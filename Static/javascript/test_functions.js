var question_answer_list={};
var question_count = 0;
var test_functions= ( function(){
    var create_initial_page = function(){
        console.log("project_ID: "+file_variables.project_ID)
        // Create a new form, then add a checkbox question, a multiple choice question,
        // a page break, then a date question and a grid of questions.

        //file_information = localStorage.getItem("project_detail");
        //console.log(JSON.parse(file_information));
        file_variables.project_ID = localStorage.getItem("current_project_ID");
        file_variables.input_path = localStorage.getItem("project_detail_input");
        file_variables.output_path = localStorage.getItem("project_detail_output");;
        file_variables.algorithm_path = localStorage.getItem("project_detail_algorithm");;


        filePath = file_variables.output_path+"1_1.json";
        console.log("processing json")

        //load text to right side
        $.getJSON( filePath, function( data ) {
            var items = [];
            $.each( data, function( key ) {
                console.log(data[key]['0']);
                question_answer_list[key] = data[key]['0'];
            });
            question_count = 1;
            $("#question_content").html( question_answer_list[question_count]["question"]);
            $("#answer_content").html( question_answer_list[question_count]["answer"]);
        });

        $(document).ready(function() {

    
            $.ajax({
                url : file_variables.input_path+"1_1.txt",
                success : function (data) {
                    $("#left_frame").html(data);
                }
            });




/*
            $.ajax({
                url : file_variables.output_path+"Q_1_1.txt",
                success : function (data) {
                    $("#question_content").html(data);
                }
            });
            $.ajax({
                url : file_variables.output_path+"A_1_1.txt",
                success : function (data) {
                    $("#answer_content").html(data);
                }
            });
*/

        }); 
    };
    var get_next = function(){
        console.log("show next quesiton and andswer")

        var keys = Object.keys(question_answer_list);
        var len = keys.length;
        question_count = question_count +1;
        if(question_count <= len ){
            $("#question_content").html( question_answer_list[question_count]["question"]);
            $("#answer_content").html( question_answer_list[question_count]["answer"]);
        }        
    }
    var postToGoogle = function () {
        console.log("send data to google spreadsheet");
/*
        var field1 = $("input[type='radio'][name='qs1']:checked").val();
        var field2 = question_count;
     
        $.ajax({
          url: "https://docs.google.com/spreadsheets/d/1_TihxgGg5dFG9jJLNeeZbZyxWwbe1ivGlvdjSdBQoMY",
          data: {
            "entry.924752166": field1,
            "entry.997497831": field2
          },
          type: "POST",
          dataType: "xml",
          statusCode: {
            0: function() {
              //Success message
            },
            200: function() {
              //Success Message
            }
          }
        });
  */
    }
    return {
        create_initial_page:create_initial_page,
        postToGoogle:postToGoogle,
        get_next: get_next
    }
})();