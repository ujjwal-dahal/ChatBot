const RenderTextArea = ({ label, name, rows = 4, formik }) => {
  const hasError = formik.touched[name] && formik.errors[name];

  return (
    <div className="flex flex-col space-y-1">
      <label
        htmlFor={name}
        className="text-sm font-semibold text-gray-200 tracking-wide"
      >
        {label}
      </label>
      <textarea
        id={name}
        name={name}
        rows={rows}
        value={formik.values[name]}
        onChange={formik.handleChange}
        onBlur={formik.handleBlur}
        className={`w-full px-4 py-2 rounded-lg bg-gray-700 border ${
          hasError ? "border-red-500" : "border-gray-600"
        } text-white placeholder-gray-400 transition duration-300 focus:outline-none focus:ring-2 ${
          hasError ? "focus:ring-red-500" : "focus:ring-indigo-500"
        }`}
        placeholder={`Enter ${label.toLowerCase()}...`}
      ></textarea>
      {hasError && (
        <p className="text-red-500 text-sm mt-1 font-medium">
          {formik.errors[name]}
        </p>
      )}
    </div>
  );
};

export default RenderTextArea;
