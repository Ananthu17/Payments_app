
$(function(){
    
    $('#rised').on('click',()=>{
        $('.toast').toast('show');
    });

    setTimeout(function(){
        if ($('#msg')) {
            $('#msg').remove()
        }
    },2000)
    const doc = new jsPDF();
    let specialElementHandlers = {
        '#print-btn': function (element, renderer) {
            return true;
        }
    };

    $('#submit').click(function () {
        console.log('adasdasd')
        doc.fromHTML($('#print').html(), 15, 15, {
            'width': 170,
            'elementHandlers': specialElementHandlers
        });
        
        doc.save('pdf-version.pdf');
    });

   
 

})


