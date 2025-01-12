import asyncHandler from "../utils/asyncHandler.js";
import wasteModel from "../models/waste.model.js";
import { ApiError } from "../utils/apierror.js";
import { cloudresult } from "../utils/Cloudinary.js";
import ApiResponse from "../utils/ApiResponse.js";
import mongoose from "mongoose";


const classifyWaste = asyncHandler(async (req, res) => {
    const { label, degradability, quantity } = req.body;
  
    // Validate input
    if (!label || !degradability) {
      throw new ApiError(400, "Label and degradability are required.");
    }
  
    // Create waste document
    const waste =  new wasteModel({ label, degradability });
    await waste.save();
  
    let analysis = {};
    if (degradability === "degradable") {
      const manureProduced = (quantity || 1) * 0.5; 
      analysis = {
        manure: manureProduced,
        process: "Composting",
        message: `Estimated manure: ${manureProduced} kg`,
      };
    } else {
      analysis = {
        recycle: true,
        message: "Consider recycling or donating to recycler communities.",
      };
    }
  
    // Example: Optionally set some cookie for client tracking
    const options = {
      httpOnly: true,
      secure: true,
    };
    res.cookie("wasteAnalysis", JSON.stringify(analysis), options);
  
    // Send response
    res.status(201).json(new ApiResponse(201, { waste, analysis }, "Waste classified successfully."));
  });