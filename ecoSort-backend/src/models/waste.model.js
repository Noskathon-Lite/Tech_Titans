import mongoose from "mongoose";

const wasteSchema = new mongoose.Schema({
  label: { type: String, required: true },
  degradability: { type: String, enum: ["degradable", "non-degradable"], required: true },
},{
    timestamps:true
});

const wasteModel = mongoose.model("waste", wasteSchema);

export default  wasteModel;