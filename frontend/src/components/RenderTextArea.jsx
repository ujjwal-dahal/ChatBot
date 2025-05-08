const RenderTextArea = ({ label, name, rows = 3, formik }) => {
  return (
    <>
      <div>
        <label className="block text-sm font-medium text-gray-300 mb-1">
          {label}
        </label>
        <textarea
          rows={rows}
          name={name}
          value={formik.values[name]}
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          className="w-full px-4 py-2 bg-gray-700 border border-gray-600 text-white rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
        ></textarea>
        {formik.touched[name] && formik.errors[name] && (
          <p className="text-red-500 text-sm mt-1">{formik.errors[name]}</p>
        )}
      </div>
    </>
  );
};

export default RenderTextArea;
