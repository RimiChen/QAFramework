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

        //load text to right side
        $(document).ready(function() {
            $.ajax({
                url : file_variables.input_path+"1_1.txt",
                success : function (data) {
                    $("#left_frame").html(data);
                }
            });

            $.ajax({
                url : file_variables.output_path+"Q_1_1.txt",
                success : function (data) {
                    $("#right_question").html(data);
                }
            });
            $.ajax({
                url : file_variables.output_path+"A_1_1.txt",
                success : function (data) {
                    $("#answer_content").html(data);
                }
            });

        }); 
    };
    var postToGoogle = function () {
        console.log("send data to google spreadsheet");
        /*
        var field1 = $("input[type='radio'][name='qs1']:checked").val();
        var field2 = $('#feed').val();
     
        $.ajax({
          url: "https://docs.google.com/forms/d/e/1FAIpQLSdjOTKRb7YiWi8OGPq6M6CRL0TpuAsUKacKp2XgruMbIp4wzg/formResponse",
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
        postToGoogle:postToGoogle
    }
})();