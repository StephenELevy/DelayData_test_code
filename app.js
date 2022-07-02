// var btn = d3.select('#predict-btn');
// btn.on("click", function handleClick() {}

d3.select('#predict-btn').on("click", function handleClick() {
    var input1 = d3.select("#input1").property("value");
    var input2  = d3.select("#input2").property("value");
    var input3  = d3.select("#input3").property("value");
    var input4  = d3.select("#input4").property("value");
    var input5  = d3.select("#input5").property("value");
    var input6  = d3.select("#input6").property("value");
    var input7  = d3.select("#input7").property("value");
    var input8  = d3.select("#input8").property("value");
    var input9  = d3.select("#input9").property("value");
    var input10  = d3.select("#input10").property("value");
    var input11  = d3.select("#input11").property("value");
    var input12  = d3.select("#input12").property("value");
    var input13  = d3.select("#input13").property("value");
    var input14  = d3.select("#input14").property("value");
    var input15  = d3.select("#input15").property("value");
    var input16  = d3.select("#input16").property("value");
    var input17  = d3.select("#input17").property("value");
    var input18  = d3.select("#input18").property("value");
    var input19  = d3.select("#input19").property("value");

    console.log(input1);
    console.log(input2);
    console.log(input3);
    console.log(input4);
    console.log(input5);
    console.log(input6);
    console.log(input7);
    console.log(input8);
    console.log(input9);
    console.log(input10);
    console.log(input11);
    console.log(input12);
    console.log(input13);
    console.log(input14);
    console.log(input15);
    console.log(input16);
    console.log(input17);
    console.log(input18);
    console.log(input19);

    d3.json('/predictonesample/${input1}|${input2}|${input3}|${input4}|${input5}|${input6}|${input7}|${input8}|${input9}|${input10}|${input11}|${input12}|${input13}|${input14}|${input15}|${input16}|${input17}|${input18}|${input19}', function(error,items) {
        var  selector = d3.select("#result");

        console.log(items);
        selector.text(items);


    });
});