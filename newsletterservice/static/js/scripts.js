$(document).ready(function() {

    $('#filterBirthday').on('click', function() {
        var today = new Date();
        var nextMonth = new Date();
        nextMonth.setMonth(today.getMonth() + 1);

        var isFiltering = $(this).hasClass('filtering');

        if (isFiltering) {
            $('.subscriber-checkbox').each(function() {
                $(this).closest('.checkbox').show();
            });
            $(this).removeClass('filtering btn-secondary').addClass(
                'btn-info');
            $(this).text('Подписчики с ДР в ближайший месяц');

        } else {
            $('.subscriber-checkbox').each(function() {
                var subscriberId = $(this).val();
                var subscriberData = window['subscriber' + subscriberId];
                if (subscriberData) {
                    var birthDate = new Date( subscriberData.birth_date );
                    birthDate.setFullYear(today.getFullYear());
                    if (birthDate >= today && birthDate <= nextMonth) {
                        $(this).closest('.checkbox').show();
                    } else {
                        $(this).prop('checked', false);
                        $(this).closest('.checkbox').hide();
                    }
                }
            });
            $(this).addClass('filtering btn-secondary').removeClass('btn-info');
            $(this).text('Сбросить фильтрацию');
        }
    });

    $('#id_send_later').on('change', function() {
        var sendLaterValue = $(this).val();
        var currentTime = new Date();
        var sendTime = new Date(sendLaterValue);

        if (sendTime > currentTime) {
            $('#sendLaterButton').prop('disabled', false);
            $('#sendButton').prop('disabled', true);
        } else {
            $('#sendLaterButton').prop('disabled', true);
            $('#sendButton').prop('disabled', false);
        }
    });

    $('#newsletterForm').on('submit', function(e) {
        e.preventDefault();
        $.ajax({
            type: 'POST',
            url: newsletterFormUrl,
            data: $(this).serialize(),
            success: function(response) {
                alert(response.message);
                $('#newsletterForm')[0].reset();
                $('#sendLaterButton').prop('disabled', true);
                $('#newsletterModal').modal('hide');
            },
            error: function(xhr, errmsg, err) {
                alert('Ошибка отправки');
            }
        });
    });
});
