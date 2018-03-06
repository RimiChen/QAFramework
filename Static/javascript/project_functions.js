var project_functions= ( function(){
    var create_initial_page = function(){
        file_variables.project_ID = localStorage.getItem("current_project_ID");
        console.log("project_ID: "+file_variables.project_ID)

    };
    var set_input_path = function(){
        console.log("set input file path")
        file_variables.input_path = "./projects/"+file_variables.project_ID+"/input/";
        console.log("project_input: "+file_variables.input_path)
    };
    var set_output_path = function(){
        console.log("set output file path");
        file_variables.output_path = "./projects/"+file_variables.project_ID+"/output/";
        console.log("project_output: "+file_variables.output_path)
    };
    var set_algorithm_path = function(){
        console.log("set algorithm path (python file)")
        file_variables.algorithm_path = "./projects/"+file_variables.project_ID+"/algorithm/";
        console.log("project_algorithm: "+file_variables.algorithm_path)
        
    };
    var execute_algorithm = function(){
        //send request to python file and execute the algorithm
        localStorage.setItem("project_detail_input", file_variables.input_path);
        localStorage.setItem("project_detail_output", file_variables.output_path);
        localStorage.setItem("project_detail_algorithm", file_variables.algorithm_path);
        
        window.location.href='./test_page';
    }
    return {
        create_initial_page:create_initial_page,
        set_input_path: set_input_path,
        set_output_path: set_output_path,
        set_algorithm_path:set_algorithm_path,
        execute_algorithm:execute_algorithm
    }
})();