# Shropcheer:


<img src="/workspace/Shropcheer/assets/images/amiresponsive.png" width="600" height="100%">


Shropcheer is a positive news blog for local communities within Shropshire and has been created as a full-stack framework project, built using Django, Python, HTML and CSS. 

The live application can be viewed here : 

https://shropcheer-2a6907e40b3b.herokuapp.com/


# Purpose and Target Audience:
 **Problem Statement:** Within Shropshire, local newspapers are difficult to access. The largest local online news publication, The Shropshire Star website, is now hidden behind a paywall and the second largest publication, the Telford Journal, is now reducing its circulation. Another problem I have identified, is that  many online news outlets and social media algorithms have a tendency to push clickbait or negative news stories because research shows that angrier people are more likely to engage with posts and stay on the page for longer.

**Purpose:** Shropcheer will address both of these issues by hosting free to read, positive news stories about the local area. The aim is to highlight and celebrate the various communities within Shropshire in order to engender a positive feeling about local areas and enhance community spirit.

**Target Audience:** The target audience is mainly local residents of Shropshire, however this may also be a good resource for people looking at moving into the area.



# User Stories:

## Admin:

* As an admin I want to be able to be able to create, edit and delete stories so that I can maintain the website

## Site User (not logged in):

* As a site user I want to be able to browse through news stories so that I can enjoy reading content and find out if the site is for me.
* As a site user I want to know which area the article is focussed on so that I can tell if the article applies to my community. 
* As a non logged-in user I want to be able to create an account so that I can post my own content. 

## Site User (logged in):

* As a logged-in user I want to be able to post my own positive news stories so that I can share more positive stories with the local community. 
* As a logged-in user I want to be able to add images to my stories so they are more visually stimulating for the readers.
* As a logged-in user I want to be able to edit my stories so that I can provide updates or correct mistakes. 
* As a logged-in user I want to be able to delete my stories so that I can control the content that I am posting on the website.
* As a logged in user I want to be able to comment on a story so that I can interact with the author or other readers. 



## Wireframe & Initial Design:
### Home Page
<img src="/workspace/Shropcheer/assets/wireframes/shropcheerhomeNLI.png">

### Home Page Logged in navbar change - User can now add a story and logout
<img src="/workspace/Shropcheer/assets/wireframes/shropcheerhomeloggedin.png">

### Story Detail Page
<img src="/workspace/Shropcheer/assets/wireframes/shropcheerstorydetials.png">

### Add a Story
<img src="/workspace/Shropcheer/assets/wireframes/shropcheeraddstory.png">



## Agile:
This project was created using Agile principles via a projectboard on Github. The visual representation of tasks,
which were determined from the user stories, were a useful tool to map progress and understand which sections of 
the project needed to be worked on next. Defining acceptance criteria within each user story helped to make sure that 
all neccesary features and funtionality were implemeted. This method also helped to ensure that all features were crucial
to the core aims of the project, and time was not wasted on tasks that did not work towards these objectives. 

<img src="/workspace/Shropcheer/assets/images/userstories.png">


# Design Choices:

## Colour scheme:

Colour themes of blue and yellow were selected as these are the county colours that appear on the county flag of Shropshire. These colours will appear more as accents however, as there will be a minimalist design to not detract from the stories themselves. Main site background will be white to give some balance to the brightness of the blue and yellow. The yellow gives a positive, sunny and upbeat impression, matching the positive aims of the project. 

<img src="/workspace/Shropcheer/assets/images/shropshire.png" width="400" height="50%">

The colours are also reminiscent of the ‘BELIEVE’ sign in Ted Lasso, which is about a coach inspiring and bonding a team through a positive attitude. 

<img src="/workspace/Shropcheer/assets/images/Believe.jpg" width="400" height="50%">




Header / Navbar - Yellow - #ffdc00

Shropcheer Brand - Blue - #3a0fe7

Buttons - Mostly Blue - #3a0fe7 - although next and previous page buttons are yellow to stand out from the blue footer

Footer - Blue - #3a0fe7


## Typography:
Londrina Solid has been used for the name / brand, and has been lightened in weight. This was to make it closer to the weight and font style of the Ted Lasso ‘BELIEVE’ sign which is referenced in the colour scheme section.

Didact Gothic was chosen as the main text font as it gives a simple and clean look which is very easily readable in large bodies of text, whilst 
still maintaining a modern and fun look. 

This font pairing was recommened on https://fontjoy.com/

<img src="/workspace/Shropcheer/assets/images/ShropcheerFonts.png">





## Priority Features:

### Home Page:

#### Navbar & Hero Image:
![home](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/4f033ade-4485-40c2-ac2d-5fc5641b5cb7)

The landing page provides an introduction to the website with a call to action button encouraging new users to sign up. Signing up and logging in allows them access to view the available books and to add a book to the collection.
The navigation bar is valuable for users as it provides quick and easy access to important sections of the website. The navigation bar includes links to Home, Books, Add a Book, Register/Logout and Sign In. Displaying a hero image using graphics are both aesthetic and a nod to the repurposed phone booths that have been transformed into local libraries around the world.


#### Registration:

Registration allows users to view the available books and the relevant book details at The Book Booth library. It allows them to add a book as well as edit and delete their addition to ensure the book collection available is updated regularly. 

![signup](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0b6b2b83-d426-4e63-805b-09a6dcdde550)



#### Sign In:

![sign-in](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/6a1d9a16-2211-4403-88a1-3ec1b506cef4)


#### Books:

![books](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/54c96d8e-6bc3-403f-a8ad-1c4188b60a6e)


#### Add a Book:

![add a book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/8e15c1d9-193f-4032-b147-0969c3b45bab)


The form allows users to easily add a book to the library which will then be visible on the  books page for the users to browse. Users are also able to edit and delete a book they themselves have added giving them full control over their own contributions.


#### Book Details:

![book detail](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e88f0274-670b-4a76-8ef8-7c44a5f440a7)

Users are able to find more information about the book they are interested in. The book details include the title, author and a brief summary of the book along with an book cover image. This provides users with sufficient information about the book.

#### Footer:

![footer](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/fde543e6-0ee2-4c17-b8a8-436d4e824f4d)

Links in the footer redirect to respective social media pages. 
It allows users to stay connected with the The Book Booth on social media platforms, keeping them informed about any changes that may occur over time.


# Future Features:

* Implement a review system so readers can share their thoughts about books that they have completed. This will give others a better idea of whether the book is a good fit for them. 
* Display if a book is available with a status (Available, Not Available).
*  Allow users to reserve a book beforehand.
* A search engine where users can search for books by title, author and genre.
* Provide locations of nearest libraries.
* Provide a way for the users to engage and form a secure community.
* Include an about page to inform others of how The Book Booth Library works and how to use it.


Database Design:

![ERD](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/6db92c85-0b4c-485c-b60d-709df3fb963e)


Entity Relationship Diagrams (ERD) help the developer to make connections between databases and information. Creating an ERD helped me understand how the tables relate to one another. I used LucidChart to create the diagram and the arrow represent how the data fields relate to one another.


## Data Models:


| Book   |            |   |
|----------|:-------------:|------:|
| Title |  CharField |  |
| Author |  CharField   |   FK |
| ISBN | CharField |     |
| User |  CharField | FK |
| Genre |  CharField   |   FK |
| Language | CharField |  FK   |
| Summary |  TextField |  |



| Genre   |            |   |
|----------|:-------------:|------:|
| Category |  CharField | FK |


| Language   |            |   |
|----------|:-------------:|------:|
| Language |  CharField | FK  |

| Author  |            |   |
|----------|:-------------:|------:|
| Name |  CharField | FK  |

## User Flow Chart:
![The Book Booth Flowchart](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/7727f007-8e2e-45fc-b955-57e2d50d1e98)

The Flowchart served as an efficient way to make important decisions when creating the app. It helped me narrow down which decisions were important for the users and admin as well as establishing the appropriate authentication. It also helped me decide which features were the most important i.e adding a book and viewing a list of books that are available to borrow at The Book Booth Library.

# Validation
## HTML

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2F) | ![home page validate](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/2ba0ff6e-6159-47e9-ad4c-2fe954589ca8) | Pass: button is a descendant of a tag |
| Books | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fbooks%2F) | ![Validate Books page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/b7c018c4-a68a-43ee-97c5-778658bbf705) | Pass: No Errors |
| Add a Book | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Fbooks%2Fadd_book%2F) | ![validate adda book page](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/95eb01b9-22fc-43c4-93de-0ebcd1263467) | Pass: No Errors |
| Sign In| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Flogin%2F) | ![validate sign in](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/872629ce-e50d-4870-845b-ed699f9178dc) | Pass: No Errors |
| Register| [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2Faccounts%2Fsignup%2F) | ![validate sign up](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c5e042af-b3d5-4718-bc50-ef319ba1a1c3) | unclosed elements main and div |

 ## CSS

 I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.
 
| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthebookbooth1-559d9131718c.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=enhttps://jigsaw.w3.org/css-validator/validator) | ![validate css](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/200fc160-1092-4cd0-bba4-2ab1a721eb72) | Pass: No Errors |

## Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/run.py) | ![screenshot]![forms py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/f299346f-bb44-43a2-a8a5-868373d753e3)
 | Pass: No Errors |
| settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/boutique-ado/settings.py) | ![screenshot]![settings py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/7951202c-2d55-4adb-90d6-8fef0707c82c)
 | Pass: No Errors |
| Book views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/blog/views.py) | ![screenshot]![views py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/4f545d53-b304-4600-b9fb-d4feb93b6c93)
 | Pass: No Errors |
| Book urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/checkout/urls.py) | ![screenshot]![urls py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e3f52187-1f65-4171-b1ba-e9096d1b5fc0)
 | Pass: No Errors |
|  models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/hiboibrahim/thebookbooth1/main/profiles/models.py) | ![screenshot]![models py](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/f3438ec1-f275-44b6-847d-48a93c0466ed)
 | Pass: No Errors |

# Responsiveness:
Development tools were used to test responsiveness on varying sized devices including laptop, mobile and tablet size.

Full testing was performed on the following devices:

Laptops:

* Macbook Air 2018 13.3-inch screen
* Lenovo Thinkpad 14" screen

 Mobile Devices:
* Google Pixel 4a

 * Browser Compatibility:
 
 I have tested the site using the following browsers:

* Google Chrome

![chrome](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/545ba4e5-c7bc-4fd8-8660-1444dcb3be2a)


* Microsoft Edge

![microsoft edge](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/1570a9cd-6591-45db-840b-ecbe7f7aeb5b)


I can confirm that the site is responsive and looks as expected good on different screen sizes.


Mobile devices:

![Screenshot_20231207-234024](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0f0b0d7d-a72f-43a4-8a57-bc1cf02a1367)

![Screenshot_20231207-234033](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/4c3cc202-b8f6-4f9d-b1bd-cf57c911db65)

![Screenshot_20231207-234013](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/39989e07-4e8d-4faf-8b57-e11686792b38)


![0](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/211095bf-ffac-42ca-b1c8-2a45d8444038)

![Screenshot_20231207-234117 (1)](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e52d022b-d3fb-4f6c-8fcb-092386ce566b)

![Screenshot_20231208-000014](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0cd224f9-b46e-4db9-9260-999cc63fff90)





Tablet Devices:


![homepage](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/5e6eb5c7-4aba-434c-8ed8-8bfd56632f8a)

![signup tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c5f5a237-83ee-4ef3-b9b0-444f648ca225)

![sign in tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/9ac1d08b-d4b8-4aa5-a65b-e46040f3b60b)

![books tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/a9c42d34-a49a-48ed-97ba-660c02de3543)

![tabletadd](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/b516d61d-6e21-460a-b7f4-5b18abf41d00)

![bookdetails tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/17a0f099-ae15-4b8a-887b-254beac2dbb0)





# Testing:

## Lighthouse Audit:

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.


* On a laptop:

Home

![homeaudit](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/5fa9bac2-d4bf-47fe-bb4a-50b3b0c4938b)

Books 

![auditbooks](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/d6401b01-e4d5-4ed1-b8e9-ff6d5eeb4bd9)

Add a book 
![audit add book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e429ee62-ecbe-4b2f-8521-28da15773a46)

On a mobile device:

Home 
![audit home mobile ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/348889e3-8c4e-41d4-b1c6-2c974780e23b)

Books
![auditbooks](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/fad662af-54da-45d0-b381-c0d70955e4e4)

Add a book 
![audit addbookmobile](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/634965ca-1b9d-4aa1-bd17-bda89f9fbafe)


## Links

| Link | Expected Outcome | Grade |
| ------- | ---------------- | ----- |
| Logo | Navigates to the home page when clicked | Fail |
| Home | Navigates to the home page when clicked | Pass |
| Books | Navigates to a book list  page when clicked | Pass |
| Add a Book | Navigates to a form to add a book when clicked | Pass |
| Register | Navigates to a registration form when clicked | Pass |
| Log in | Navigates to a screen where users can log in when clicked | Pass |
| Logout | Navigates to a page confirming for the user to log out | Pass |

## Testing 


| Feature | Expected Outcome | Grade | Screenshots |
| ------- | ---------------- | ----- | --------- |
| Modal | A message will appear informing the user of a successful action | Pass | ![modal sign out ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/9e8658e8-f751-4cdf-be3d-ca19ad6c47b2)
| User logged in | Text displays the user logged in with their username | Pass | ![modal sign in name](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/cc4a71db-9962-49c1-b4b6-563000687ad7)
| View books | Users can see available books which have been added | Pass | ![testing books](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/01cc3a5b-db46-4742-a8e1-cf715d78c89b)
| Add a book | Add a book to the book collection that will be available to borrow | Pass | ![addbook](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/82133f44-d43a-4f40-863a-f4e8970057aa)
| Admin has access to crud functionality of all additions | Admin can edit or delete any book addition | Pass | ![admin testing](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/72df0b87-6d4f-4659-9d4f-5e986f88e16c)
| Edit a book | A user can edit the details on the book that they have addded. It will update their addition on the books page | Pass | ![edit book ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/79f6de7e-fd14-4c34-a474-483b7cd5285f)
| Delete a book | A user who added a book OR an admin can delete a book. It will then be deleted from the DB | Pass | ![delete book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/88275723-e875-404a-b96f-58bac0a4907a)
| Registration | New users can access a registration form from the "Register" link | Pass | ![testing sign up](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e9e6c4e1-c90a-4854-a11c-014a8fc80043)
| Log in | Users can log in using a form after clicking "Log in" | Pass | ![sign in testing ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/3fafee34-e6d6-4162-8989-faa78e1bf355)
| Log out | Users get logged out after clicking "Log out" | Pass | ![testing sign out](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/d7d377aa-fc2d-4025-a73e-22d2d81c622a)
| Grid display | A CSS grid will display the books in a clear, responsive format | Pass | N/A
| Functional buttons | Edit, delete, create buttons will be functional throughout the site | Pass | ![edit delete buttons](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/67cfb78d-7d5b-4072-8aa8-812b9c444b67)
| Footer | A footer displays social information | Pass | ![footer](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0879fada-18a4-4363-8257-0af0061cf79f)
| Social links work | The social links will navigate to a new page when they're clicked. They will open in a new tab | Pass | ![footer](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0879fada-18a4-4363-8257-0af0061cf79f)


# Tools and Technologies Used:
The technologies implemented in this application included HTML5, CSS, Bootstrap, Python and Django.

* Python used as the back-end programming language.
* Git used for version control. (git add, git commit, git push)
* GitHub used for secure online code storage.
* GitHub Pages used for hosting the deployed front-end site.
* Gitpod used as a cloud-based IDE for development.
* Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.
* ElephantSQL used as the Postgres database.
* Heroku used for hosting the deployed back-end site.
* Cloudinary used for online static file storage.
* Canva Utilized for collaborative design and prototyping(wireframes).

* Google and Stack Overflow utilized for general research or solving a bug, information gathering, and various online tools.


# Languages Used:
* HTML5
* CSS
* Python

# Deployment :

I used the steps used when deploying our django blog to deploy this application. The instructions for this mainly came from the follow along videos and text-steps provided on the code institute LMS.

# Bugs

All the bugs that occured during the creation of this application have been resolved. There is a section of the application which allows you to reset your password that needs to be implemented, however they were not within the scope of this particular project and will be addressed in the near future along with the other future features.


# Credit: 

* Although I used the django blog resources provided on the LMS, I also received alot of additional clarification by following along with django projects on YouTube. One of the vidoes I found especially helpful was : https://youtu.be/JzDBCZTgVyw?si=w3BBwJswUjBTm1xw

* Stack Overflow was used to solve any smaller bugs and further clarification on errors I was receiving in the terminal.

* I used this site to generate a persona and created user stories: https://founderpal.ai/user-persona-generator

* A special thanks to all the other indivudals in our cohort for their continuous support throughout the course.

* The added book covers and details were taken from the Waterstones Website.

* Font Awesome was used for icons and the fonts used were derived from Google Fonts.

* Wireframes, logo and flowcharts were created using Canva. 
