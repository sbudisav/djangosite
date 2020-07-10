$('a.like').click(function(e){
  e.preventDefault();
  console.log("click registered")
  $.post('{% url "posts:like" %}',
    {
      id: $(this).data('id'),
      action: $(this).data('action')
    },
    function(data){
      if (data['status'] == 'ok')
      {
        var previous_action = $('a.like').data('action');

        // toggle data-action
        $('a.like').data('action', previous_action == 'like' ? 'unlike' : 'like');
        // toggle link text
        $('a.like').text(previous_action == 'like' ? 'Unlike' : 'Like');

        // update total likes
        var previous_likes = parseInt($('span.count .total').text());
        $('span.count .total').text(previous_action == 'like' ? previous_likes + 1 : previous_likes - 1);
      }
    }
  );
});