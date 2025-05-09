"use client";

import RenderInput from "@/components/RenderInput";
import RenderTextArea from "@/components/RenderTextArea";
import axios from "axios";
import { useFormik } from "formik";
import { useState } from "react";
import { useRouter } from "next/navigation";
import * as Yup from "yup";
import TrainProgress from "@/components/TrainProgress";

export default function FormPage() {
  const [isTraining, setIsTraining] = useState(false);
  const router = useRouter();

  const formik = useFormik({
    initialValues: {
      user_name: "",
      company_name: "",
      location: "",
      founded_year: "",
      about_company: "",
      product_and_services: "",
      greeting_message: "",
      thanks_message: "",
      epoch: "",
    },
    validationSchema: Yup.object({
      user_name: Yup.string().required("Please enter your name."),
      company_name: Yup.string().required("Please provide the company name."),
      location: Yup.string().required("Please specify the company location."),
      founded_year: Yup.string().required("Please enter the founding year."),
      about_company: Yup.string()
        .min(50, "At least 50 characters.")
        .required("Tell us about the company."),
      product_and_services: Yup.string().required(
        "Please describe the products and services offered."
      ),
      greeting_message: Yup.string().required("Greeting message is required."),
      thanks_message: Yup.string().required("Thanks message is required."),
      epoch: Yup.string().required("Epoch must be provided."),
    }),

    onSubmit: (values) => {
      sendFormData(values);
    },
  });

  const sendFormData = async (data) => {
    try {
      await axios.post("http://127.0.0.1:8000/api/", data);
      setIsTraining(true);
      await axios.post("http://127.0.0.1:8000/api/train-bot/");
    } catch (error) {
      console.error("Error:", error.message);
      alert("Something went wrong while training the bot.");
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 flex items-center justify-center p-4">
      <div className="bg-gray-800/90 backdrop-blur-md shadow-2xl rounded-3xl p-10 w-full max-w-4xl border border-gray-700">
        <h1 className="text-4xl font-semibold mb-10 text-center text-white">
          Company Information Form
        </h1>

        {isTraining ? (
          <TrainProgress />
        ) : (
          <form onSubmit={formik.handleSubmit} className="space-y-8">
            {/* Basic Info */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <RenderInput label="User Name" name="user_name" formik={formik} />
              <RenderInput
                label="Company Name"
                name="company_name"
                formik={formik}
              />
              <RenderInput label="Location" name="location" formik={formik} />
              <RenderInput
                label="Founded Year"
                name="founded_year"
                type="number"
                formik={formik}
              />
            </div>

            {/* Descriptions */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <RenderTextArea
                label="About Company"
                name="about_company"
                rows={5}
                formik={formik}
              />
              <RenderTextArea
                label="Product & Services"
                name="product_and_services"
                rows={5}
                formik={formik}
              />
            </div>

            {/* Messages */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <RenderInput
                label="Greeting Message"
                name="greeting_message"
                formik={formik}
              />
              <RenderInput
                label="Thanks Message"
                name="thanks_message"
                formik={formik}
              />
            </div>

            {/* Epoch */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <RenderInput
                label="Epoch"
                name="epoch"
                type="number"
                formik={formik}
              />
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              className="w-full py-3 rounded-xl font-medium bg-indigo-600 hover:bg-indigo-700 text-white"
            >
              Train Bot
            </button>
          </form>
        )}
      </div>
    </div>
  );
}
