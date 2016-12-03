$(document).ready(function(){
	var actAns = [2,3,4,2,1];
	var ans = [];
	$('#uname').focusout(function(){
		var uname = $('#uname').val();
      	if(uname.length > 2){
      		$('.equestions').show();
      		$('#q1').show();
      	}
	});
	$('#qsubmit').click(function(){
		ans[0] = $('input[name="q1"]:checked').val();
		ans[1] = $('input[name="q2"]:checked').val();
		ans[2] = $('input[name="q3"]:checked').val();
		ans[3] = $('input[name="q4"]:checked').val();
		ans[4] = $('input[name="q5"]:checked').val();
		var nCorrect = 0;
		for(var i = 0 ; i <= 4 ; i++){
			if(ans[i] == actAns[i]){
				nCorrect += 1;
			}
		}
		// Calcuating Result
		var correctWidth = nCorrect*100;
		if(nCorrect == 5){
			$('.g-correct').css('border-radius','4px');
		}
		if(nCorrect == 0){
			$('.g-wrong').css('border-radius','4px');
		}
		$('.g-correct').css('width',correctWidth+'px');
		$('.g-wrong').css('width',(500-correctWidth)+'px');
		var per =  nCorrect*100/5
		var wr = 100 - per
		if(per > 0){
			$('.g-correct').html(per+' % Correct');
		}else{
			$('.g-correct').html('');
		}
		if(per < 100){
			$('.g-wrong').html(wr+' % Wrong');
		}else{
			$('.g-wrong').html('');
		}
		//Showing Graph
		$('.egraph').show();
		// Showing Result
		$('.result-in').html('');
		$('.result-in').append(
					'<div class="result-item result-top">'+
						'<div class="result-col col1">Question</div>'+
						'<div class="result-col col2">Your Answer</div>'+
						'<div class="result-col col3">Actual Answer</div>'+
						'<div class="result-col col4">Result</div>'+
					'</div>'
					);
		for(var i = 0 ; i <= 4 ;i++){
			var result = 'wrong';
			if(ans[i] == actAns[i]){
				result = 'correct';
			}
			$('.result-in').append(
				'<div class="result-item result-'+result+'">'+
					'<div class="result-col col1">'+(i+1)+'</div>'+
					'<div class="result-col col2">'+$('.a'+(i+1)+ans[i]).html()+'</div>'+
					'<div class="result-col col3">'+$('.a'+(i+1)+actAns[i]).html()+'</div>'+
					'<div class="result-col col4">'+result+'</div>'+
				'</div>'
				);
		}
		$('.eresult').show();
	});

	$(document).on('keyup','#uname',function(e){
		var key = e.which || e.keyCode;
	    if (key == 13) { 
	      	var name = $('#uname').val();
	      	if(name.length > 2){
	      		$('.equestions').show();
	      		$('#q1').show();
	      	}
	    }
	});

	$('input[name=q1]').change(function(){
		$('#q2').show();
	});
	$('input[name=q2]').change(function(){
		$('#q3').show();
	});
	$('input[name=q3]').change(function(){
		$('#q4').show();
	});
	$('input[name=q4]').change(function(){
		$('#q5').show();
	});
	$('input[name=q5]').change(function(){
		$('.submit-outer').show();
	});
});