function showPanel(id) {
  if(id === "session_btn") {
    document.getElementById('analyze_div').style.display = "none";
    document.getElementById('build_div').style.display = "none";
    document.getElementById('build2_div').style.display = "none";
    document.getElementById('session_div').style.display = "block";
    document.getElementById(id).classList.add('chosen');
    document.getElementById('build_btn').classList.remove('chosen');
    document.getElementById('build2_btn').classList.remove('chosen');
    document.getElementById('analyze_btn').classList.remove('chosen');
  }
  if(id === "build_btn") {
    document.getElementById('session_div').style.display = "none";
    document.getElementById('build2_div').style.display = "none";
    document.getElementById('analyze_div').style.display = "none";
    document.getElementById('build_div').style.display = "block";
    document.getElementById(id).classList.add('chosen');
    document.getElementById('session_btn').classList.remove('chosen');
    document.getElementById('build2_btn').classList.remove('chosen');
    document.getElementById('analyze_btn').classList.remove('chosen');
  }
  if(id === "build2_btn") {
    document.getElementById('session_div').style.display = "none";
    document.getElementById('analyze_div').style.display = "none";
    document.getElementById('build_div').style.display = "none";
    document.getElementById('build2_div').style.display = "block";
    document.getElementById(id).classList.add('chosen');
    document.getElementById('session_btn').classList.remove('chosen');
    document.getElementById('build_btn').classList.remove('chosen');
    document.getElementById('analyze_btn').classList.remove('chosen');
  }
  if(id === "analyze_btn") {
    document.getElementById('session_div').style.display = "none";
    document.getElementById('build_div').style.display = "none";
    document.getElementById('build2_div').style.display = "none";
    document.getElementById('analyze_div').style.display = "block";
    document.getElementById(id).classList.add('chosen');
    document.getElementById('build_btn').classList.remove('chosen');
    document.getElementById('build2_btn').classList.remove('chosen');
    document.getElementById('session_btn').classList.remove('chosen');
  }
}

function chooseOption(id) {
  console.log('chosen');
  const modelForm = document.getElementById('model');
  alert(modelForm.elements["model"].value);
  const phi = document.getElementById('phi');
  const lk = document.getElementById('lk');
  const kx = document.getElementById('kx');
  const temp = document.getElementById('temp');
  const buildForm = document.getElementById('build');
  //console.log(model.value + ' ' + option.value);
  const formData = {
    model: modelForm.elements["model"].value,
    phi: phi.value,
    lk: lk.value,
    kx: kx.value,
    temp: temp.value,
    build: buildForm.elements["model-build"].value
  };
  localStorage.setItem('formData', JSON.stringify(formData));
  window.open('/' + id);
}

function testFunction(arg) {
  console.log(arg);
}
