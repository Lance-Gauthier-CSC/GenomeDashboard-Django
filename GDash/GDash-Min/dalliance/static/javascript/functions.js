function getFormData() {
  const formData = JSON.parse(localStorage.getItem('formData'));
  localStorage.removeItem('formData');
  // console.log(formData);
  // const formModel = formData.model;
  // const formOption = formData.option;
  // console.log(formModel);
  // console.log(formOption);
  document.getElementById('info').innerHTML = "<p>" + JSON.stringify(formData) + "</p>";
}
