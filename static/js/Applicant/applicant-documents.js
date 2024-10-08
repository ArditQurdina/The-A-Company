$(document).ready(function() {
    $('.open-popup').click(function() {
    var number = $(this).data('number');
    $('#document_id').val(number);
    $('.bg-add-and-edit, .popup').css("display", "flex");
    var titleValue = $(this).attr('title');
    console.log(titleValue);

    // Store the selected "open-popup" element
    selectedPopup = $(this);

    $('.name-document').text(titleValue);
    console.log(number);

    $('.save-submit-input').off('click').on('click', function() {
        if (selectedPopup) {
            if ($("#id_document")[0].files.length > 0) {
                $('.bg-add-and-edit, .popup').css("display", "none");
                var titleText = $(selectedPopup).attr('title');
                var modifiedTitleText = titleText.replace("Upload", "Download");

                // Set a data attribute on the selectedPopup to store the uploaded file
                selectedPopup.data('uploadedFile', $("#id_document")[0].files[0]);

                selectedPopup.closest('.main-div-docs').find('.mutual-titles-color').addClass("blue-text");
                selectedPopup.attr('src', '../img/documents-second-icon.svg');
                selectedPopup.attr('title', modifiedTitleText);

                // Create the download link if it doesn't exist
                // Set the download link properties
                $(selectedPopup).on('click', function() {
                    $('.bg-add-and-edit, .popup').css("display", "none");
                    var uploadedFile = selectedPopup.data('uploadedFile');
                    if (uploadedFile) {
                        var downloadLink = document.createElement('a');
                        downloadLink.href = URL.createObjectURL(uploadedFile);
                        downloadLink.download = uploadedFile.name;
                        downloadLink.style.display = 'none';
            
                        document.body.appendChild(downloadLink);
                        downloadLink.click();
                        document.body.removeChild(downloadLink);
                    }
                });
            }
        }
    });

    // Unbind previous click event handlers and add a new one
});

//   });
  $(document).ready(function() {
    $(".bg-add-and-edit").click(function() {
        $(this).hide();
    $('#upload-form')[0].reset(); // Reset the form
    fileList.innerHTML="or drag and drop it here";
    });
});

  $('#id_document').on('change', function() {
    var fileInput = this.files[0];

    if (fileInput) {
      // Check the file extension
      var allowedExtensions = ['.pdf', '.jpg', '.jpeg', '.png', '.svg'];
      var fileExtension = fileInput.name.slice(((fileInput.name.lastIndexOf(".") - 1) >>> 0) + 2);
      if (allowedExtensions.indexOf('.' + fileExtension.toLowerCase()) === -1) {
        // Invalid file extension, update the input border color
        $('#id_document').css('border', '2px solid red');
        $('#error').css('display', 'block');
        $('#error').css('color', 'red');
      } else {
        // Reset the input border color if the file is valid
        $('#error').css('display', 'none');

        $('#id_document').css('border', '1px solid #ffff');
      }
    }
  });

});

        
                const dropArea = document.getElementById('drop-area');
                const fileInput = document.getElementById('id_document');
                const fileList = document.querySelector('#second-line');
                let uploadedFile = null;
        
                dropArea.addEventListener('dragover', (e) => {
                    e.preventDefault();
                    dropArea.style.backgroundColor = '#f0f0f0';
                });
        
                dropArea.addEventListener('dragleave', () => {
                    dropArea.style.backgroundColor = 'red';
                });
        
                dropArea.addEventListener('drop', (e) => {
                    e.preventDefault();
                    dropArea.style.backgroundColor = '#ffffff';
                    const file = e.dataTransfer.files[0];
                    handleFile(file);
                });
        
                fileInput.addEventListener('change', () => {
                    const file = fileInput.files[0];
                    handleFile(file);
                });
        
                function handleFile(file) {
                    // Clear previously uploaded file
                    fileList.innerHTML = '';
                    uploadedFile = null;
        
                    if (file) {
                        fileList.innerHTML=`${file.name}`;
                        uploadedFile = file;
                    }
                }
        
                function formatSize(bytes) {
                    if (bytes < 1024) {
                        return bytes + " bytes";
                    } else if (bytes < 1048576) {
                        return (bytes / 1024).toFixed(1) + " KB";
                    } else if (bytes < 1073741824) {
                        return (bytes / 1048576).toFixed(1) + " MB";
                    } else {
                        return (bytes / 1073741824).toFixed(1) + " GB";
                    }
                }
        
                // Add a click event listener to the drop area to trigger the file input
                dropArea.addEventListener('click', () => {
                    fileInput.click();
                });


                $(document).ready(function() {
                    var mobileMediaQuery = window.matchMedia('(max-width: 890px)');
                    var overMobileMediaQuery = window.matchMedia('(min-width: 891px)');
                    $('.job-left-row').click(function() {

                        if (mobileMediaQuery.matches) {
                        $('.job-left').hide();
                        $('.right-jobs-main-div').show();
                        
                        $('.your-work-permit-is-here-form-content').hide();
                        $('.profileHeader').hide();
                        $('.main-buttons-div').hide();

                    };
            

            if (overMobileMediaQuery.matches) {
                        $(".job-left-row").removeClass("different-background-jobs");
                // Add the 'active' class to the clicked div
                $(this).addClass("different-background-jobs");
            }
                        var Applicantnumber = $(this).data('number'); // Get the number from the data attribute of the clicked button
                        var index = $(this).data('number');

                        $('.documents-for-work-permit-form-content').data('sourceDiv', $(this));
            $('#applicantID').val(Applicantnumber); // Set the value of the input field in your popup
    

          

            $('.your-work-permit-is-here-form-content').hide();
            
                    })

                    $('.myjob-right-exit').click(function() {
                            if (mobileMediaQuery.matches) {
                                $('.job-left').css("display", "block");
                                $('.right-jobs-main-div').css("display", "none");
                                $('.profileHeader').show();
                                $('.main-buttons-div').show();
                                $(".job-left-row").removeClass("different-background-jobs");


                            }
                        })
                    $('.documents-for-work-permit-form-content').click(function() {
    // Get the source .div element
    var sourceDiv = $(this).data('sourceDiv');
    
    // Check if the sourceDiv is defined
    if (sourceDiv) {
      // You can access the index of the source div if needed
      var index = $('.job-left-row').index(sourceDiv);
      console.log('Opened from .job-left-row clicked index: ' + index);
    }
  });

    });

    $(document).ready(function() {
        
        if (window.innerWidth >= 891){
            $('.job-left-row').eq(0).click();
        }
    });

$(".under-container-mutual-mutual-stats").click(function(event) {
        event.stopPropagation();
});