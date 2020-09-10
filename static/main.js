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
            var previous_likes = parseInt($('span.total[data-id=' + like.dataset.id +']').text());
            $('span.total[data-id=' + like.dataset.id +']').text(previous_action == 'like' ? previous_likes + 1 : previous_likes - 1);
          }
        }
      );
    };
  });

  document.querySelectorAll('a.follow').forEach(function(follow) {
    follow.onclick = function(e) {
      $.post($(this).data('url'),
        {
          id: follow.dataset.id,
          action: follow.dataset.action
        },
        function(data){
          if (data['status'] == 'ok')
          {
            var previous_action = $(follow).data('action');

            // toggle data-action
            $(follow).data('action', previous_action == 'follow' ? 'unfollow' : 'follow');
            
            // toggle link text
            $(follow).text(previous_action == 'follow' ? 'Unfollow' : 'Follow');
          }
        }
      );
    };
  });
});
