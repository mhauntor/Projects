$(document).ready(function () {
    var selectedFoods = [];

    $("#add-button").click(function () {
        var selectedFood = $("#food-select option:selected");
        var foodName = selectedFood.text();
        var calorie = parseFloat(selectedFood.val());
        var weight = parseFloat(selectedFood.data("weight"));
        var protein = parseFloat(selectedFood.data("protein"));
        var fats = parseFloat(selectedFood.data("fats"));
        var carbohydrates = parseFloat(selectedFood.data("carbohydrates"));

        if (foodName && calorie && weight && protein && fats && carbohydrates) {
            selectedFoods.push({
                name: foodName,
                calorie: calorie,
                weight: weight,
                protein: protein,
                fats: fats,
                carbohydrates: carbohydrates
            });
            updateSelectedFoods();
            calculateTotal();
            calculateTotalCalories();
        }
    });

    $("#selected-foods").on("click", ".cancel-button", function () {
        var index = $(this).data("index");
        selectedFoods.splice(index, 1);
        updateSelectedFoods();
        calculateTotalCalories();
        calculateTotal();
    });

    function updateSelectedFoods() {
        var selectedFoodsTable = $("#selected-foods tbody");
        selectedFoodsTable.empty();

        for (var i = 0; i < selectedFoods.length; i++) {
            var foodItem = selectedFoods[i];
            var row = $("<tr>");
            row.append($("<td>").text(foodItem.name));
            row.append($("<td>").text(foodItem.weight));
            row.append($("<td>").text(foodItem.calorie));
            row.append($("<td>").text(foodItem.protein));
            row.append($("<td>").text(foodItem.fats));
            row.append($("<td>").text(foodItem.carbohydrates));
            var cancelButton = $("<button>")
                .text("X")
                .addClass("cancel-button")
                .data("index", i);
            row.append($("<td>").append(cancelButton));
            selectedFoodsTable.append(row);
        }
    }

    function calculateTotal() {
        var totalweight = 0;
        var totalCalorie = 0;
        var totalProtein = 0;
        var totalFats = 0;
        var totalCarbohydrates = 0;
        for (var i = 0; i < selectedFoods.length; i++) {
            totalweight += selectedFoods[i].weight;
            totalCalorie += selectedFoods[i].calorie;
            totalProtein += selectedFoods[i].protein;
            totalFats += selectedFoods[i].fats;
            totalCarbohydrates += selectedFoods[i].carbohydrates;
        }
        $("#total-weight").text(totalweight);
        $("#total-calorie").text(totalCalorie);
        $("#total-protein").text(totalProtein);
        $("#total-fats").text(totalFats);
        $("#total-carbohydrates").text(totalCarbohydrates);
    }
});