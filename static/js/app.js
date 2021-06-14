// (function ($, document, window) {

// 	$(document).ready(function () {

// 		function setCountDown() {

// 			// set the date we're counting down to
// 			var target_date = new Date($(".counter-wrap").data("date-target")).getTime();

// 			// variables for time units
// 			var days, hours, minutes, seconds;

// 			// update the tag with id "countdown" every 1 second
// 			setInterval(function () {

// 				// find the amount of "seconds" between now and target
// 				var current_date = new Date().getTime();
// 				var seconds_left = (target_date - current_date) / 1000;

// 				if (current_date < target_date) {
// 					// do some time calculations
// 					days = (parseInt(seconds_left / 86400) < 10) ? "0" + parseInt(seconds_left / 86400) : parseInt(seconds_left / 86400);
// 					seconds_left = seconds_left % 86400;

// 					hours = (parseInt(seconds_left / 3600) < 10) ? "0" + parseInt(seconds_left / 86400) : parseInt(seconds_left / 86400);
// 					seconds_left = seconds_left % 3600;

// 					minutes = (parseInt(seconds_left / 60) < 10) ? "0" + parseInt(seconds_left / 60) : parseInt(seconds_left / 60);
// 					seconds = (parseInt(seconds_left % 60) < 10) ? "0" + parseInt(seconds_left % 60) : parseInt(seconds_left % 60);
// 				} else {
// 					days = '00';
// 					hours = '00';
// 					minutes = '00';
// 					seconds = '00';
// 				}
// 				// format countdown string + set tag value

// 				$(".days .number").html(days);
// 				$(".hours .number").html(hours);
// 				$(".minutes .number").html(minutes);
// 				$(".seconds .number").html(seconds);

// 			}, 1000);

// 		}

// 		setCountDown();

// 		new WOW().init();
// 	});

// 	$(window).load(function () {

// 	});

// })(jQuery, document, window);

// from data.js
var tableData = data;

var selectCompany = d3.select("#company");

// Get the companies from the data
var companiesMapped = tableData.map(companies => companies.company);

var companyPlaceHolder = selectCompany.append("option").html('<i class="fa fa - building - o"></i>Company');

companiesMapped.forEach((comp) => {
	selectCompany.append("option").text(comp);
});

// get the last set of inputs and refill into form
try {
	// retrieve the last set of inputs
	var inputMovie = d3.select("#input_movie").text();
	var inputPopularity = d3.select("#input_popularity").text().replace(/,/g, "");
	var inputBudget = d3.select("#input_budget").text().replace(/,/g, "").replace("$", "");
	var inputDay = d3.select("#input_day").text();
	var inputYear = d3.select("#input_year").text();
	var inputLangauge = d3.select("#input_language").text();
	var inputDuration = d3.select("#input_duration").text();
	var inputCountry = d3.select("#input_country").text();
	var inputGenre = d3.select("#input_genre").text();
	var inputCompany = d3.select("#input_company").text();
	var inputDirector = d3.select("#input_director").text();
	var inputWriter = d3.select("#input_writer").text();
	var inputActor = d3.select("#input_actor").text();

	// refill the input fields with the previous inputs
	d3.select("#moviename").attr("value", inputMovie);
	d3.select("#popularity").attr("value", inputPopularity);
	d3.select("#budget").attr("value", inputBudget);
	d3.select("#day").attr("value", inputDay);
	d3.select("#year").attr("value", inputYear);
	d3.select("#language").attr("value", inputLangauge);
	d3.select("#duration").attr("value", inputDuration);
	d3.select("#country").attr("value", inputCountry);
	d3.select("#genre").attr("value", inputGenre);
	d3.select("#company").attr("value", inputCompany);
	d3.select("#director").attr("value", inputDirector);
	d3.select("#writer").attr("value", inputWriter);
	d3.select("#actor").attr("value", inputActor);



} catch (err) { // catch any errors
	console.log("Not enough values defined!");
};