/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imageResult')
                .attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
		
		validateForm();
    }
}

function validateForm() {
	console.log("validateForm called")
	var imageInput = document.getElementById('chooseFile');
	var descInput = document.getElementById('comment');
	
	if (imageInput.files && imageInput.files[0] && descInput.value) {
		document.getElementById("saveChangesButton").disabled = false;
	}
	else {
		document.getElementById("saveChangesButton").disabled = true;
	}
}

function uploadForm() {
	var formData = new FormData();
	formData.append('csrfmiddlewaretoken', window.CSRF_TOKEN);
	formData.append('image', document.getElementById('chooseFile').files[0], document.getElementById('chooseFile').files[0].name);
	formData.append('date', document.getElementById('saveInfoDate').textContent);
	formData.append('desc', document.getElementById('comment').value);
	
	var xhr = new XMLHttpRequest();
	xhr.open('POST', '/submitForm', true);
	xhr.onload = function () {
		if (this.status === 200)
			console.log(this.response);
		else
			console.error(xhr);
	};
	xhr.send(formData);
}

$(function () {
    $('#chooseFile').on('change', function () {
        readURL(document.getElementById('chooseFile'));
    });
});

$(function () {
    $('#comment').on('change', function () {
        validateForm();
    });
});