|start| main [
    
    |init| "Hello World" -> text;

    |while| true [
        |invoke| print: text;
        |exit|
    ];
]