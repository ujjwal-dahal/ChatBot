"use client";

import RenderInput from "@/components/RenderInput";
import RenderTextArea from "@/components/RenderTextArea";
import axios from "axios";
import { useFormik } from "formik";
import { useState } from "react";
import * as Yup from "yup";

export default function FormPage() {
  const [formData, setFormData] = useState({});

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
    },
    validationSchema: Yup.object({
      user_name: Yup.string().required("Please enter your name."),
      company_name: Yup.string().required("Please provide the company name."),
      location: Yup.string().required("Please specify the company location."),
      founded_year: Yup.string().required(
        "Please enter the year the company was founded."
      ),
      about_company: Yup.string()
        .min(
          50,
          "Please provide a more detailed description (at least 50 characters)."
        )
        .required("Tell us about the company."),
      product_and_services: Yup.string().required(
        "Please describe the products and services offered."
      ),
      greeting_message: Yup.string().required(
        "A greeting message is required to welcome users."
      ),
      thanks_message: Yup.string().required(
        "Please include a message to thank your users."
      ),
    }),

    onSubmit: (values) => {
      setFormData(values);
      sendFormData(values);
    },
  });

  const sendFormData = async (data) => {
    try {
      let response = await axios.post("url", data);
      console.log(response.data);
    } catch (error) {
      console.log("Error Message : ", error.message);
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 flex items-center justify-center p-4">
      <div className="bg-gray-800 shadow-2xl rounded-2xl p-8 w-full max-w-3xl">
        <h1 className="text-3xl font-bold mb-6 text-center text-white">
          Company Information Form
        </h1>

        <form onSubmit={formik.handleSubmit} className="space-y-6">
          {/* Basic Info */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
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

          {/* Company Description */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <RenderTextArea
              label="About Company"
              name="about_company"
              rows={4}
              formik={formik}
            />
            <RenderTextArea
              label="Product & Services"
              name="product_and_services"
              rows={4}
              formik={formik}
            />
          </div>

          {/* Messages */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
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

          <button
            type="submit"
            className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition duration-300"
          >
            Train Bot
          </button>
        </form>
      </div>
    </div>
  );
}
