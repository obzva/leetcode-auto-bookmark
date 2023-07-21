# leetcode-auto-bookmark
## What is this for?
This tool frees you from repetitive clicking tasks when you need to to bookmark a lot of problems at Leetcode! 

# Installation & Preparation
## Installation
1. `git clone` this project

```bash
git clone https://github.com/obzva/leetcode-auto-bookmark.git
```

2. Change the current working directory to the project folder

```bash
cd leetcode-auto-bookmark
```

3. Make the venv and activate it

```bash
python -m venv venv && source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

## Preparation
Before get started you need to do three things

1. Login to Leetcode and get `LEETCODE_SESSION` cookie
2. Make your list where you want to collect the bookmarked problems into
3. Get the list of problem links

### 1. Login to Leetcode and get `LEETCODE_SESSION` cookie
Login to Leetcode and follow these steps

1. Open devtools and go to Applications tab
2. Go to cookies
3. Get the value of the cookie whose key is `LEETCODE_SESSION`
<img width="966" alt="image" src="https://github.com/obzva/leetcode-auto-bookmark/assets/98512859/ac29ee5c-8a33-495a-9eff-36d59f20dea6">

### 2. Make your list where you want to collect the bookmarked problems into
If you aleready made one, you can skip this part

1. Click the profile badge from main page it will show popover below. Click `My List` from that popover
<img width="1255" alt="image" src="https://github.com/obzva/leetcode-auto-bookmark/assets/98512859/ec20eee3-0725-4226-99e7-a57a4751ac0f">
2. Click the `+` button next to the text *My List* and create your new list

### 3. Get the list of problem links
You need a `text.txt` file that contains a list of problem links. The logic inside app will automatically extract the `https` links, so make sure that your text file contains only links that is a valid leet code problem.

For example this is valid text file.
```txt
Hello,
I have been solving all two pointers tagged problems in last 3.5 months, and wanted to share my findings/classifications here. If you are preparing for technical interview, two pointers is one of the popular topics that you can't skip :).

There are around 140 problems today, but I only solved the public ones (117 problems).
Majority of them is in easy or medium so, if you understand the basic ideas then it should be solvable without much hints and editorials.

I see 4 bigger categories and many sub categories in it, and marked the typical example problems with (*).
I would recommend you to start solving these example problems, and apply the knowledge to the other problems. I don't want to copy & paste my ugly codes here, you would easily find fantastic solutions from the problem discussion page.


1. Running from both ends of an array
The first type of problems are, having two pointers at left and right end of array, then moving them to the center while processing something with them.
image

2 Sum problem
(*) https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
https://leetcode.com/problems/3sum/
https://leetcode.com/problems/4sum/
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
https://leetcode.com/problems/sum-of-square-numbers/
https://leetcode.com/problems/boats-to-save-people/
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
https://leetcode.com/problems/3sum-with-multiplicity/
```

After you've got proper list of links, save it as `text.txt` file into the project root!

# Execution
Execute this CLI command in the project root.
```bash
python app.py
```

or

```
sudo python app.py
```

The CLI will ask you three inputs; **leetcode-session-token**, **listname**, **action**

For **leetcode-session-token**, copy and paste the *cookie value* you've got

For **listname**, type the name of the list you want to collect the problems into

For **actions**, type `Add` if you want to add the problems into the list or type 'Remove' if you want to remove the problems from that list

For example, this command will let the app to login to Leetcode via $sample-values$ and then add problems into $sample-list$

```bash
sudo python app.py
Password:
leetcode-session-token: $sample-value$
listname: $sample-list$
action ( Add / Remove ): Add
```

