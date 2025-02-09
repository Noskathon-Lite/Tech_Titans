import { Schema, model } from "mongoose";
// import {
//   generateAccessToken,
//   generateRefreshToken,
// } from "../services/token.service.js";
// import bcrypt from "bcrypt";

const wasteSchema = new Schema(
  {
    dustbinId: {
      type: Schema.Types.ObjectId,
      ref: "Dustbin", // Reference to the User model
      required: true,
    },
    category: {
      type: String,
      required: true,
      enum: ["plastic", "paper", "bottle", "cardboard", "other"],
      trim: true,
      maxLength: 30,
    },
    type: {
      type: String,
      required: true,
      trim: true,
      enum: ["biodegradable", "non-biodegradable"],
      maxLength: 30,
    },
    image: {
      type: String,
      required: true,
    },
  },
  {
    timestamps: true,
  }
);

//create a table
const Waste = model("Dustbin", wasteSchema);

export default Waste;
