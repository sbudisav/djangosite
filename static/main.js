document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('a.like').forEach(function(like) {
    like.onclick = function(e) {
      $.post($(this).data('url'),
        {
          id: like.dataset.id,
          action: like.dataset.action
        },
        function(data){
          if (data['status'] == 'ok')
          {
            var previous_action = $(like).data('action');
            // toggle data-action
            $(like).data('action', previous_action == 'like' ? 'unlike' : 'like');
            // toggle link text
            $(like).text(previous_action == 'like' ? 'Unlike' : 'Like');

            // update total likes
            var previous_likes = parseInt($('span.count .total').text());
            $('span.count .total').text(previous_action == 'like' ? previous_likes + 1 : previous_likes - 1);
          }
        }
      );
    };
  });
});
