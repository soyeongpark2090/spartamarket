# 👩‍💻Project: Sparta Market
#### 내일배움캠프 AI 6기: 파이썬 웹 프레임워크인 django를 활용해서 Sparta Market을 구현해본 개인과제

<br>

## 👨‍🏫 Project Introduction
팔고싶은 물건을 게시하고, 그에 대해 LIKE를 누를 수 있는 기본적인 형태의 중고거래 사이트

<br>

## ⏲️ Development time
- 2024.04.14(월) ~ 2023.04.19(금)


<br>

## 💻 Development Environment
- **Programming Language** : Python 3.10
- **Web Framework** : DJANGO
- **Database** : SQLite (for development and testing)
- **IDE** : Visual Studio Code
- **Version Control** : Git, GitHub
  
<br>

## 📝 Project Result

![스크린샷 2024-04-19 125848](https://github.com/soyeongpark2090/spartamarket/assets/159408752/e7b67405-1bb5-4127-9809-9c92d5dee004)


<br>


## 📌 Key Features

### 1. Auth
   - 회원가입, 로그인, 로그아웃, 회원정보 수정, 회원탈퇴 기능
   - 로그인이 된 사용자에게는 '로그아웃','회원정보 수정', '회원탈퇴'버튼이 노출되며, 그렇지 않은 경우에는 '로그인'버튼과 '회원가입'버튼이 노출된다

### 2. Product_Post CRUD
   - 사용자는 자신이 팔고자 하는 물품에 대한 게시글(이미지 포함)을 작성할 수 있고, 자신이 작성한 게시물에 한해서 수정,삭제가 가능하다
   - 게시물 조회는 메인페이지인 전체 게시물 목록 페이지에서 가능하며, 로그인하지 않은 비회원도 열람할 수 있다
   - 게시물 목록 페이지의 카드 링크를 클릭하면 해당 물품에 대한 상세 페이지로 이동할 수 있다
   - 게시물의 작성자가 회원탈퇴를 할 경우에 그가 작성한 게시물도 모두 자동으로 삭제된다

### 3. Comment CRD
   - 물품의 상세 페이지 하단에서 게시글에 대한 댓글을 작성,수정,삭제할 수 있다.
   - 댓글의 작성자에 한해 수정,삭제가 가능하며, 자신이 작성한 댓글에 대해서만 수정버튼과 삭제버튼이 보여진다
     
### 4. LIKE
   - 사용자들은 다른 유저들이 작성한 게시글에 LIKE(찜)를 누를 수 있다
   - 메인페이지인 전체 게시물 목록에 있는 카드 내에 있는 하트표시를 눌러서 찜(LIKE)을 할 수도, 찜을 해제할 수도 있다
     
### 5. Profile Page & Follow
   - 게시물의 상세 페이지에 있는 작성자를 클릭하면, 작성자의 프로필 페이지로 이동할 수 있다
   - 각 유저의 프로필 페이지에는 그가 작성한 게시글 목록과 LIKE를 누른 게시글의 목록을 볼 수 있고, 하이퍼링크를 통해 해당 게시글 페이지로 바로 이동할 수 있다
   - 프로필 페이지 상단에는 해당 유저에 대한 Follow버튼이 있으며, 버튼을 눌러서 팔로우할 수도 있고, 언팔로우 할 수도 있다
   - Follow버튼 하단에는 해당 유저의 팔로잉과 팔로워 수가 표시된다

<hr>

### 1. Auth
  - Allows users to register, log in, log out, modify their information, and withdraw membership.
  - Provides appropriate buttons based on user authentication status, such as 'Logout', 'Edit membership information', 'Withdraw membership', 'Login', and 'Sign up'.

### 2. Product_Post CRUD:
  - Enables users to create, read, update, and delete posts (including images) about items they want to sell.
  - Posts are accessible on the main page, full post list page, and can be viewed by non-members.
  - Allows navigation to detailed item pages by clicking on card links.

### 3. Comment CRD:
  - Provides functionality to create, read, and delete comments on posts.
  - Only allows comment authors to edit or delete their comments.

### 4. LIKE:
  - Allows users to like posts written by other users.
  - Users can like or unlike posts by clicking the heart symbol on the main page.


### 5. Profile Page & Follow:
  - Users can navigate to an author's profile page by clicking on their name.
  - Profiles display lists of posts made by the user and posts liked by the user, with hyperlinks to relevant post pages.
  - Includes a Follow button to follow or unfollow users.
  - Shows the number of followers and following users at the bottom of the Follow button.
     


