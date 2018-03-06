var initialize_setting = ( function(){
    var create_initial_page = function(){
        console.log("create initial page, frames");
        console.log("add setting files")
        console.log("load exist projects")
    };
    var create_new_project = function(){
        // in this function
        //create new botton for project
        console.log("add new botton for new project")
        generate_new_empty_project();
        //console.log("create project folder")
        console.log("create setting file")

        // redirect to project page
        //save project ID
        
    }
    var load_projects = function(){
        console.log("load setting files, to add old porject")
    }
    var link_to_project_page = function(project_name){
        console.log("create and prepare project page");
        console.log("python call");
    }
    function generate_new_empty_project(){
        //generate project ID
        console.log("generate a new project ID and folders");
        new_project_ID = create_project_ID();
        //crate empty project
        let new_project = new project(new_project_ID)
        //create folder for projects
        console.log("create project folder")
        create_folder_through_python(new_project_ID)
        
        return new_project_ID;
    }
    function create_folder_through_python(new_project_ID){
        //trigger python file to create folders
        $.post( "/folder_operation", {
            javascript_data: new_project_ID
        });
    }
    function create_project_ID(){
        return "test_new_project_ID";
    }
    return {
        create_initial_page:create_initial_page,
        create_new_project:create_new_project,
        load_projects:load_projects,
        link_to_project_page:link_to_project_page 
    }
})();