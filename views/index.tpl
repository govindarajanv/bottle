% if len(uploads) > 0:
<h1> List of uploads </h1>
<ul>
 % for upload in uploads:
        <li> <a href="/uploads/{{upload}}">{{upload}}</a></li>
 % end
</ul>
% else:
    <h1> You dont have any uploads </h1>
% end