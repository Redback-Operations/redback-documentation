---
sidebar_position: 3
---

# **Section 2 - Coding Best Practices**

This section explains a variety of coding best practice methods that we can try and apply to our work to achieve a variety of goals.

::: Info
Author: **Lachlan Harrison**, **03/05/2025**
:::

On top of mitigating the code smells, we also need to ensure that we are also implementing some coding best practices to avoid security vulnerabilities and ensure that our code is appropriately utilized. Having these standards matter as it achieves numerous accomplishments including: 

- ***Consistency:*** We can ensure uniformity across codebases which makes it easier for developers to read, understand and maintain our code. Applying the same concepts throughout our code effectively being concise.

- ***Readability:*** Having well-defined standards can reduce errors raised and improves collaboration within the team as everyone is able to easily read the code.

- ***Error Prevention:*** With consistent practices, we can catch some common mistakes early reducing the risk of bugs being existent and improving our coding quality.

- ***Scalability:*** Adhering to our best standards ensures our code can scale without becoming unmanageable. In other words, we can keep our performance in mind while coding and deliver a solution with good performance throughout the coding process.

- ***Cross-Team Collaboration:*** We can facilitate collaboration among developers especially in large teams. For example, Redback Operations being a large team and collaborating on various coding projects. Any member can look at your code, understand what is occurring and even contribute to the solution.

- ***Code Reviewing:*** An important aspect of this module, code reviews provide a clear criterion which can lead to effective feedback and refactoring of code in which we can then simplify our code. (This will be a dedicated section further in the module)

- ***Efficient Maintenance:*** Following our standards will simplify the debugging process within our coding alongside refactoring and maintenance tasks for our projects.


Within this section of the module, we will briefly go through some various methods in which we can implement to our own coding to achieve the above accomplishments.

#### 1.	**Have security and privacy considerations:**
With constant threats emerging, we want to mitigate any risk of any potential compromise. In saying this, having security considerations is of extreme importance and needs to always be implemented within our code. Some things we should not be doing at all, and this also comes with our code reviewing is:

- **NO** Hardcoded passwords
- **NO** Hardcoded usernames
- **NO** Sensitive data coded or listed

These three main points are a definite ‘no-go’ within coding as these can be easily leveraged against us and can often lead to attacks against our systems and unauthorised access. After all, most cyber security incidents are often caused by human error, so mitigating this risk can drastically reduce the likelihood of a compromise leading to an incident. These also come from secure coding practices including studying and analysing the OWASP Top 10, MITRE ATT&CK Framework, Cryptography Measures (Encryption/Decryption) and Security by design. Some resources will be provided for further information:

- **OWASP Top 10:** https://owasp.org/www-project-top-ten/
- **MITRE:** https://attack.mitre.org/

The main priority with this coding standard is that we should always be thinking about security considerations while completing our work, not have it as an afterthought. 
Always keep a tight security posture and always question to yourself, “Am I giving away any sensitive information in this file?”


#### 2.	**Focus on Code readability:**
With code readability, there are various elements in which we can incorporate with our coding to improve the readability of the code in which can be very useful and simple to implement. These tactics involve: Writing as few lines as possible within our code, utilizing appropriate naming conventions, segment our blocks of code in the same section into paragraphs, utilizing indentation to mark the beginning and end of our control structures, not using lengthy functions as a single function should carry out a single task (this falls into the bloater code smell), using the DRY principle (Don’t Repeat Yourself), automate repetitive tasks whenever possible and avoiding long lines of code.
Some examples of this include:
```
//Hard to read code: (C#)
public void hardToReadCode(num, start, end)
{
int mid=start+end/2;
if num==null return null;
else result = mid+num*2;
return result;
}
```
```
//More readable code: (C#)
public void easierToReadCode(num, start, end)
{
    int mid = start+end/2;
    if num == null
    {
        return null;
    }
    else
    {
        result = mid+num*2;
        return result;
    }
}
```
- With indentations in this example we are able to easier identify elements within a function. Readability is the key focus for this outcome!


#### 3.	**Having meaningful names:**
We can utilize lots of different naming conventions within our coding and keep it consistent throughout a file. (As every file is different, some users may prefer one method to another.) We typically always stick to these naming conventions as it can achieve a variety of our outcomes listed above in particular readability and consistency.
These naming conventions can be further elaborated into four main conventions:

- **Camel Case:** We start the name with a lowercase letter, if the name has multiple words, these words start with capital letters. This convention is typically utilized in JavaScript and even C# environments.
```
public void findMaxValue();
```

- **Snake Case:** We start the name with a lowercase letter, if the name has multiple words, these words start with a lowercase also and are separated with a ‘_’. This convention is typically utilized in Python environments.
```
Int student_member_number = 42;
```

- **Kebab Case:** This is similar to the snake case except instead of using ‘_’ we utilise ‘-‘. This convention is typically utilized within HTML and CSS environments.
```
get-user-input();
```

- **Pascal Case:** Also known as Upper Camel Case, we start with a capital letter, if the name has multiple words, these all start with capital letters. This convention is typically utilized in C#, Python and JavaScript environments.
```
int StudentMemberNumber = 42;
```

To summarise, when selecting a naming convention, use it throughout the entirety of developing your code and try to minimise switching throughout the project. Consistency and Readability are key here!


#### 4.	**Avoid the use of a single identifier for numerous purposes:**
Throughout our projects, we should always assign unique variable names to avoid any overlap! Especially minimise the use of global identifiers unless required as these can lead to confusion, unintended behaviour when running our programs and potential bugs within the project itself. This falls under efficient maintenance and error prevention especially if we can detect these issues early!
```
//An example of a single identifier (C#) We want global to stay as 10:
int global = 10;
public void LocalIdentifier()
{
    int local = global*2;
    global = 20; //We can easily change the global variable as it is a global variable hence the variable not needing to be initialised.
}
LocalIdentifier();
Console.WriteLine(global); //Prints 20 not 10
```
```
//An example of unique variable names (C#) We want global to stay as 10:
public void LocalIdentifier()
{
    int global = 10;
    int local = global*2;
    Console.WriteLine(global)
}
Console.WriteLine(LocalIdentifier()) //Prints 10 and not Local
```
As we can observe in our example, the `LocalIdentifier()` function in our second example keeps the `global` variable within the function and won't change. Whereas in our first example, our `global` variable is a global variable in which can always be easily changed despite us wanting to keep it as one consistent variable. Consistency is the key outcome for this practice!


#### 5.	**Add comments and prioritize documentation:**
It’s always wise to add comments to our code when writing it, there’s many benefits to doing so, but too much can make code messy and often relates back to our code smells in regards to dispensables but also our main accomplishments including readability, consistency and cross-team collaboration as comments can serve as documentation purposes also to inform other developers what is occurring, what needs to be done, etc. Here are some valid placements of when we should be adding comments versus when we should minimise it so that we don’t have too many dispensables occurring. Keeping in mind also that incorrect comments can mislead developers so we should always also be ensuring that we are accurate when writing a comment so that other developers can easily understand but also ourselves.

*WHEN TO ADD COMMENTS:*
-	When explaining intricate/non-obvious coding segments
-	Explaining business rules, regulatory requirements
-	Clarifying how the code handles edge cases/exceptions
-	Documenting workarounds due to limitations or external dependencies
-	Marking areas of improvement


*WHEN NOT TO ADD COMMENTS:*
-	Redundant comments that repeat what the code already expresses
-	If the code’s purpose is evident
-	We should remove temporary comments used for debugging once the issue has been resolved

```
//An Example of comments in action: (REMOVE) will indicate to remove the line of comments:

def function_work()
{
    //TO WORK ON
}

variable = 42 //Assigns 42 to variable (REMOVE) - Codes purpose is evident

dataset = [1,2,3,4,5] //Link to complete_function

def complete_function() //Calculate the range of the dataset (REMOVE) - Codes purpose is evident
{
    data_min = min(dataset)
    data_max = max(dataset)
    range = data_max-data_min
    return range
}
print(range) //Print the range of the dataset here once finished function (REMOVE) - Improvements have already been made so we can remove this
```


#### 6.	**Have efficient data processing:**
When we code, we want to process data efficiently to achieve a result faster than something that may take longer due to incorrect coding/larger functions. This best practice method involves looking at dividing our code into smaller functions for reusability and maintainability which also achieves efficient maintenance should it be required. What this also means is that we need to be identifying any inefficient algorithms/data structures when conducting our code reviews and refactor them to create a more efficient solution.


#### 7.	**Have effective code review and refactoring:**
We will explore this more in depth in a future section and after the remaining points of this section. Essentially, we are trying to follow consistent coding techniques, catching various points of improvement/error and refactoring to achieve these standards. We should always be double checking our work and attempting to discover any potential points of improvement or elements we may need to tweak to achieve these coding standards. After all, we all want our code to achieve an objective. Have we reviewed our code numerous times to make sure we achieve the various goals?


#### 8.	**Try to formalise exception handling:**
The term *‘exception’* refers to any problem, issue or events that can occur when the code is running and may disrupt the flow of execution. This can ultimately terminate a program early or even pause it which we always are trying to avoid when coding. Exception handling is something that may not always be required (for example documentation pages) although when we are coding for something else (for example a video game) we always want to attempt to normalise exception handling. This can be achieved in several ways including ‘Try-Catch’ blocks for example in which is typically the most common way of exception handling as we can ‘Catch’ these exceptions and see what is going wrong with the code. Sometimes also when we need to consider what is going wrong with our code, this can also come down to slowness in which sometimes, patience is key although too much time consumed with nothing occurring can be a definite issue in which remediation is required to find issues and effectively have efficient maintenance.
```
//Utilizing 'Try-Catch' (C#)
try{
    CallToFunction(element);
    Console.WriteLine("Test Passed!");
}
catch(ArgumentNullException)
{
    Console.WriteLine("Exception caught");
}
```

#### 9.	**Choose Industry-specific coding standards:**
When utilizing coding standards, we can suit the needs of what we are developing. In other words, developing a video game may typically utilize C++ for example whereas HTML, CSS and JavaScript are typically utilized for Web Development. Understanding the requirements of our objectives assists us in determining what standards we should utilize. If we are constructing a visual representation of a dataset, R or even Python may be our solution to the development process. Although, keep in mind when selecting a language that some may have various security issues in which you also need to consider and be prepared to mitigate. For example, the C++ and C languages don’t have any bound checks in which buffer overflows may occur. Always make sure that the coding language and standards you are utilising are appropriate for the solution you are developing but always consider these security considerations as well.


#### 10.	**Standardise headers for different files:**
With readability, we can create easier understandings amongst developers when the headers of different files align with a singular format. An example of this includes:
File name, Date of Creation, Name of creator of the file and a summary of what it does.

```
//Example File Name – 04/05/2025 - Student Name
//Multiplies two numbers to give a new result.

```

We can achieve this by some simple comments at the top of the file describing these various characteristics. By doing this, we also achieve cross-team collaboration as someone can open this file, read the top, and understand what is happening in the file rather than trying to decipher what the entirety of the file does. While yes, the developer may have left some comments throughout the file, having this header at the top of the file, makes it so much easier for users to quickly read and then decide if this is the file they are looking for or if they need to continue their search for something else.


#### 11.	**Ensure there is daily backups/manual saving:**
This is a simple measure that we can implement although it still can sometimes slip through. Although we always wish that our systems can never crash, sometimes this can still happen, they can crash, data loss can occur, glitches, hardware damage. All of which can affect the progress of our work. 

We should save our code daily for large projects but even for smaller files, something as simple as ***‘Ctrl+S’*** (on Windows) to save our file always ensures we are keeping our progress so that if one of these unprecedented scenarios occur, we can be confident that when we return, we can pick up our work where we left it off without fear of losing what we have worked on. Autosave can be viable but don’t always rely on it also. Manual saving after all is the key to achieving this best practice method. Always remember to keep saving your work throughout the duration of modification, don't leave it until the end of your session to save and exit!!

