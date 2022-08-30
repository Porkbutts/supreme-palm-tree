RedditClone

Users
Posts
Comments

Users create posts, comments.  Users have total number of upvotes associated w/ account.
Posts have comments from different users.  Posts are created by users and have upvote score as well.
Comments can have replies from other comments.  Comments are created by users and also have upvotes.


MongoDB Schema

User - id
Username - string
postHistory - List of Posts
commentHistory - List of Comments
postUpvotes - int (total upvotes from posts created by user)
commentUpvotes - int (total upvotes from comments created by user)

Post - id
Timestamp - Timestamp Obj
originalPoster - id of User
contentPath - string
comments - List of comments directly replying to post
upvotes - int

Comment - id
createdBy - id of user
Parent - id of comment being replied to ( or id of post if not a reply )
Root - id of comment nesting the parent ( or id of itself if it is a root)
content - string
upvotes - int
 
