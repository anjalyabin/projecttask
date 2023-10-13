<html>
<script type="text/javascript">
$(document).ready(function() {
    $('#district').change(function() {
        var district = $(this).val();
        $('#branch option').hide();
        $('#branch option.' + district).show();
    });
});
</script>
</html>