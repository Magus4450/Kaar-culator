var province = document.getElementById("id_province");
var district = document.getElementById("id_district");
var local = document.getElementById("id_local");

var button = document.getElementById("submit");

button.disabled = true;
// import * as data from './data_final.json';
const dataa = null;

fetch("/static/js/data_final.json")
  .then((response) => response.json())
  .then((data) => {
    for (var i = 0; i < Object.keys(data).length; i++) {
      console.log(Object.keys(data)[i]);
      var option = document.createElement("option");
      option.text = Object.keys(data)[i];
      option.value = Object.keys(data)[i];
      province.add(option);
    }
  });

province.addEventListener("change", () => {
  district.selectedIndex = 0;
  local.selectedIndex = 0;
  button.disabled = true;
  fetch("/static/js/data_final.json")
    .then((response) => response.json())
    .then((data) => {
      var length = district.options.length;
      for (i = length - 1; i >= 0; i--) {
        district.options[i] = null;
      }

      var option = document.createElement("option");
      option.disabled = true;
      option.selected = true;
      option.text = "-- Select District --";
      district.add(option);

      const districtData = data[province.value];
      const unique = [...new Set(districtData.map((item) => item.District))];

      for (var i = 0; i < unique.length; i++) {
        var option = document.createElement("option");
        option.text = unique[i];
        option.value = unique[i];
        district.add(option);
      }
    });
});

district.addEventListener("change", () => {
  local.selectedIndex = 0;
  button.disabled = true;
  fetch("/static/js/data_final.json")
    .then((response) => response.json())
    .then((data) => {
      var length = local.options.length;
      for (i = length - 1; i >= 0; i--) {
        local.options[i] = null;
      }

      var option = document.createElement("option");
      option.disabled = true;
      option.selected = true;
      option.text = "-- Select a Local Body --";
      local.add(option);

      const districtData = data[province.value];
      const localData = districtData.filter(
        (item) => item.District == district.value
      );

      for (var i = 0; i < localData.length; i++) {
        console.log(localData[i]);
        var option = document.createElement("option");
        option.text = localData[i]["Local Body"];
        option.value = localData[i]["Local Body"];
        local.add(option);
      }
    });
});

local.addEventListener("change", () => {
  if (local.selectedIndex != 0) {
    button.disabled = false;
  } else {
    button.disabled = true;
  }
});

const monthlySalInput = document.getElementById("id_monthly_salary");
const monthylSalError = document.getElementById("monthly_salary_error");

const employeeProvidentFundInput = document.getElementById(
  "id_employee_provident_fund"
);
const employeeProvidentFundError = document.getElementById(
  "employee_provident_fund_error"
);

const monthsInput = document.getElementById("id_months");
const monthsError = document.getElementById("months_error");

const citizenInvestmentTrustInput = document.getElementById(
  "id_citizen_investment_trust"
);
const citizenInvestmentTrustError = document.getElementById(
  "citizen_investment_trust_error"
);

const bonusInput = document.getElementById("id_bonus");
const bonusError = document.getElementById("bonus_error");

const insuranceInput = document.getElementById("id_insurance");
const insuranceError = document.getElementById("insurance_error");

function addErrorHandling(input, error, errorMessage) {
  input.addEventListener("input", () => {
    if (input.value == "") {
      button.disabled = true;
    } else if (input.value < 0) {
      button.disabled = true;
      error.innerHTML = errorMessage;
    } else if (
      monthlySalInput.value > 0 &&
      employeeProvidentFundInput.value > 0 &&
      monthsInput.value > 0 &&
      citizenInvestmentTrustInput.value > 0 &&
      bonusInput.value > 0 &&
      insuranceInput.value > 0
    ) {
      button.disabled = false;
      error.innerHTML = "";
    }
  });
}

addErrorHandling(
  monthlySalInput,
  monthylSalError,
  "Monthly Salary cannot be negative"
);
addErrorHandling(
  employeeProvidentFundInput,
  employeeProvidentFundError,
  "Employee Provident Fund cannot be negative"
);
addErrorHandling(monthsInput, monthsError, "Months cannot be negative");
addErrorHandling(
  citizenInvestmentTrustInput,
  citizenInvestmentTrustError,
  "Citizen Investment Trust cannot be negative"
);
addErrorHandling(bonusInput, bonusError, "Bonus cannot be negative");
addErrorHandling(
  insuranceInput,
  insuranceError,
  "Insurance cannot be negative"
);

// monthlySalInput.addEventListener('change', () =>{
//     if(monthlySalInput.value == ''){
//         button.disabled = true;
//     } else if(monthlySalInput.value < 0){
//         button.disabled = true;
//         monthylSalError.innerHTML = 'Monthly salary cannot be negative';
//     } else {
//         button.disabled = false;
//         monthylSalError.innerHTML = '';
//     }
// })
