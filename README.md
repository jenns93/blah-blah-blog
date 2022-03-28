# Blah Blah Blog
![]()
- [Live Website](https://blah-blah-blog-2022.herokuapp.com/)
- [Github Repository](https://github.com/jenns93/blah-blah-blog)
 # About
A place to make your case for what you think are the best Films / Tv Shows & Books!


## Table of Contents

- [User Experience UX](#User-Experience-UX)

- [Features](#Features)

- [Technologies Used](#Technologies-Used)

- [Data Model](#Data-Model)

- [Testing](#Testing)

- [Deployment](#Deployment)

- [Bugs](#Bugs)

- [Credits](#Credits)

## User Experience UX
### User Stories
i. As a Site Admin I can allow or disallow comments so that I can filter unwanted / distasteful comments.

ii. As a Site Admin I can make draft posts so that I complete content at another time.

iii. As a Site Admin I can create, read, update and delete posts so that I can manage the blog feed.

iv. As a Site User I can Like and unlike posts so that I can interact with the content.

v. As a Site User I can post comments so that I can get involved with the discussion.

vi. As a Site User I can create an account so that I can comment and like.

vii. As a Site User/Admin I can View comments on a post so that I can follow the conversation.

viii. As a Site User/Admin I can View the amount of likes on each post so that I can see the popularity of each post.

ix. As a Site user I can click on a post so that I can read the whole post.

x. As a Site User I can View a list of posts so that I can select the one I wish to view.

xi. As a Site User I can View a paginated list of posts so that I can select posts to view easily.

## Features
![Home]()
-  

![Sign Up]()
- Users will be prompted to create an account by filling in a short form.
- Users will be required to provide an email address, full name and password.
- When the form is completed usres can select "Submit" where they will be redirected to the home screen allowing them to now like / dislike and comment on posts.
- A notification bar will aprear on home page breifly to confirm Sign up succesful.
- An email will be sent to user as confimation of creating their account.
 
![Login]()
- Users will be asked to provive their email and account password.
- When required fields are completed the user can select "login" to gain access to their profile and begin using the full ameinities of the website and will be redirected to the home page.
- A notification bar will aprear on home page breifly to confirm login.
 
![Log Out]()
- Users will be asked if they are sure they would like to "Log Out" once before log out is completed and will then be redirected to the home page.
- A notification bar will aprear on home page breifly to confirm logout.

![Profile]()
- Users can view thier profile which displays their details and list of posts created.

![Creating Posts]()
- From the homepage registered users will have the option to complete the post form.
- Users will name the post, select the media type, enter the subject's title and write their post / opinion they wish to put forward.
- Once all fields are completed and the user happy they can publish their post or save as draft. 

 ![Commenting]()
- Registered users when viewing a full post will have the option to fill out the comment form and submit their thoughts on the post to discuss with other users.
- Once thier comment is submmited the users will be notified that their comment was succesfully posted.
- The users comment will now be visable to other site users and will be added to the string of comments below the original comment. 

![Like / Dislike]()
- Registered users will have the ability to Like / Dislike posts.
- Registered users can only vote to Like or Dislike a post not both. ( Users can change their mind anytime and choose the oposite option)
- Totals of Likes & Dislike will be displayed next to their repected icons. ( Counts will also be displayed on homepage list of posts)

![Flag]()
- Registered users will have the option to Flag a post if they feel the post need admin intervention.
- Flag option can be deselected if users clicked this by mistake. (Flagged status will be removed for admin as well)
- Site admin will review the flagged status and will determin if the flag was justified.
- If admin deems the flagged status of post correct then the post will be removed.

![Contact Us]()
- Registered users can direct themselves to the "Contact Us" page where they will be asked to complete the contact form.
- Users will be asked for details of their issues before submiting.
- Once completed the user will be notified of the submition of their contact form and are then redirected to the homepage. 

### Future Features
- Email users when someone has commented on thier post.
- Email users when milestone likes are achived e.g. 100, 500, 1,000 etc.
- Notify users when thier post has been flagged for review.
- Favorite button to allow users to bookmark their favorite posts.
- Most liked post of the month, highlighting the most popular posts.
- Option to follow another user to be notified when they publish a new post.
- List of top contributors of the site e.g. Most post likes, most followed.

## Technologies Used

### Languages Used

- Python
- JavaScript
- Django

### Frameworks, libraries, and programs used

-[Heroku](https://dashboard.heroku.com/apps) Heroku was used to host the files and to publish the finished program.

-[Gitpod](https://www.gitpod.io/) Gitpod was used to code the website and commit changes throughout the development to Github.

## Data Model

## Testing

### Functionality Testing

### Validator Testing 
- PEP8. No errors were returned from PEP8online.com

### Testing User Stories
i. As a Site Admin I can allow or disallow comments so that I can filter unwanted / distasteful comments.
1. Users have the ability to flag posts or comments that the admin can review for unwanted / distasteful language.

ii. As a Site Admin I can make draft posts so that I complete content at another time.
1. Posts can be saved as either: Published or Draft, allowing for post completion at a later time.

iii. As a Site Admin I can create, read, update and delete posts so that I can manage the blog feed.
1. The Admin has options to create, update and delete any posts they wish along with ability to veiw all posts Published & Draft. 

iv. As a Site User I can Like and unlike posts so that I can interact with the content.
1. Registered Users once logged in have the ability to Like or Dislike any posts they wish. ( 1 choice per user per post )

v. As a Site User I can post comments so that I can get involved with the discussion.
1. Registered Users once logged in have the ability to comment on any post as many times as they wish to allow the flow of the discution.

vi. As a Site User I can create an account so that I can comment and like.
1. Visitors have option to create an account to be eligible to use the full ameinities of the website.

vii. As a Site User/Admin I can View comments on a post so that I can follow the conversation.
1. Visitors & Registerd users can view comments on posts. However on registered users will have the ability to comment / like / dislike.

viii. As a Site User/Admin I can View the amount of likes on each post so that I can see the popularity of each post.
1. The counts of Likes & Dislikes are visible on the home page list of posts and on the post detail page.

ix. As a Site user I can click on a post so that I can read the whole post.
1. Visitors & Registerd users can view full post by selecting them from the homepage where they are redirected to the full post.

x. As a Site User I can View a list of posts so that I can select the one I wish to view.
1. Visitors & Registerd users will be presented with a list of posts on the homepage they can view. 

xi. As a Site User I can View a paginated list of posts so that I can select posts to view easily.
1. When multiple posts are avalible the homepage will pagintate to allow for neat & compact view of site.

## Deployment
### Heroku
The program has been deployed using Heroku.
#### Steps for deployment:
- Fork or clone the repository.
- Create a new Heroku app.
- Set the build backs to Python and Nodejs in this order.
- Link the Heroku app to the repository.
- Click Deploy. 

### Forking the GitHub Repository
To contribute you can Fork without affecting the main branch. Follow the instructions outlined below.

1. Go to GitHub and log in.
2. Find the Repository that was used for this project.
3. To the right of the Repository name you will see the 'Fork' button. This is located next to the 'Start' and 'Watch' buttons.
4. Doing this will place a copy in your own repository.
5. When you are finished locating the 'New Pull Request' button above the file list on the original repository.

### Cloning
- To clone or download the repository to your own device follow the instructions listed below.

1. Head to Github and log in.
2. Find the Repository for this site.
3. Below the name of the repository find the 'Clone or Download' green button.
4. To clone the repo using HTTPS click the link below "Clone with HTTPS".
5. Open your Terminal and go to the directory you want the cloned directory to be copied to.
6. Enter "Git Clone" and paste the URL copied from GitHub.
7. Create your local clone by pressing "Enter".

## Bugs
### Solved Bugs
### Remaining Bugs
- No known bugs remaining at time of writing.

## Credits

#### Code

- Code institute 
- Stackoverflow for tips, examples concepts for further understanding of language definitions.
- w3schools for tips, examples concepts for further understanding of language definitions.
- GeeksforGeeks for examples for understanding language better.

#### Content

- All code written by the author - Jack Jenns

- To create the README file inspiration was taken from:

- Code Institute [SampleREADME](https://github.com/Code-Institute-Solutions/SampleREADME)
- Code Institute [README Template](https://github.com/Code-Institute-Solutions/readme-template)
- [Markdown cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### Acknowledgements
- Stackoverflow.
- Fellow students on slack.
- My mentor for his guidance.
- W3schools. 
- GeeksforGeeks



