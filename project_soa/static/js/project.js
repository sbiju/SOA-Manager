/* Project specific Javascript goes here. */
$(function() {

    Dropzone.options.myDropzone = {

        // Prevents Dropzone from uploading dropped files immediately
        autoProcessQueue : false,
        uploadMultiple: true,
        addRemoveLinks: true,
        acceptedFiles: ".png, .jpg, .jpeg, .gif, .PNG, .JPG, .JPEG, .GIF, pdf, .doc, .docx,",
        maxFilesize: 10,

        init : function() {
            myDropzone = this;

            $("#submit-all").on("click", function() {
                myDropzone.processQueue();
                // Tell Dropzone to process all queued files.
            });

            // You might want to show the submit button only when
            // files are dropped here:
            this.on("addedfile", function() {
                // Show submit button here and/or inform user to click it.
            });

        }
    };

});