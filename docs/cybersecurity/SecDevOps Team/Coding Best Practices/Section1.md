---
sidebar_position: 2
---

# **Section 1 - Code Smells**

This section looks at various types of code smells that may arise when coding.

::: Info
Author: **Lachlan Harrison**, **03/05/2025**
:::

Code smells? It can happen, not literally though we can detect these "smells" within a developers code. Code smells are often indications of problems/violations within a developer’s design of their code that are present even when the code is deemed functional. They are not bugs or errors but are observable violations of code design. This section of the module will aim to assist you in learning about these various code smells, how they arise and what we can do to mitigate them. There are three main Code smells in which we will be looking at, these include Bloaters, Change Preventers and Dispensables. (For the purposes of understanding, we will mostly be focusing on bloaters and dispensables)

## **BLOATERS:**
The first of the code smells categories falls under Bloaters: These are often referred to as Code, functions and classes that are so large that they become harder to work with. These can often accumulate over time as programs evolve. Within bloaters some causes of this smell arise from – Long methods, large classes, long parameter lists, Data clumps and Primitive obsession. (For our demonstration, we will focus on long methods, large classes and long parameter lists.)
```
//Example of what this can look like (Python)
def large_function(data, parameter2, parameter3, parameter4, parameter5, parameter6)
{
    if(data == null)
    {
        return 0
    }
    calculate_average = sum(data)/2
    print(calculate_average)
    data_min = min(data)
    data_max = max(data)
    range = data_max - data_min
    print(range)
    data_sum = sum(data)
    print(f"Sum of data: {data_sum}")
}
dataset = [0, 1, 2, 3, 4, 5]
large_function(dataset)
```

```
//How we can minimise bloaters (Python)
def small_function(data)
{
    if(data == null)
    {
        return 0
    }
    average = sum(data)/2
    print(average)
}
def range_function(data)
{
    range = max(data)-min(data)
    print(range)
}
dataset = [0, 1, 2, 3, 4, 5]
small_function(dataset)
range_function(dataset)
```

### **CHANGE PREVENTERS:**
This relates to changing something in one place but then we must make various changes across the code. This can further complicate our code and make it less readable and less consistent. Some causes of these Change Preventers include Divergent Change, Shotgun Surgery and Parallel Inheritance Hierarchy. (This code smell is not a main focus for this module although the provided resource will allow for further investigation into this particular smell)
More can be explored via this link: https://refactoring.guru/refactoring/smells/change-preventers


## **DISPENSABLES:**
This can occur at any point throughout coding and this code smell relates to something that is unneeded in which when we refactor these, we can make the code become cleaner, efficient and easier to read. This smell can arise from many different factors in which we will go through in our examples. Dispensables is a very common code smell to occur in development. These involve Comments, duplicate code, data classes, dead code, lazy classes and speculative generality. (For our demonstration, we will focus on comments, duplicate code and dead code.)
```
//Some examples of dispensables (HTML)
<html>
<body>
<h1 id="title"> Hello World! </h1>
<script>
function unused() //Dead code
{
    console.log("Unused function");
}
function calculate(value) //Unneeded comments + Dead Code
{
    if(value < 0) //Checks if our value is less than 0
    {
        return value * 6; //Multiplies value by 6
    }
    else return value + 4; //Adds 4 to our value for everything else
}
function change('title') //Duplicate code
{
    change.style.font = 'bold';
    change.style.font = 'bold';
}
const alignment = //Lazy element
{
    Nothing:() => {}
}
</script>
</body>
</html>
```

```
//How we can minimise dispensables (HTML)
<html>
<body>
<h1 id="title"> Hello World! </h1>
<script>
function update-title('title')
{
    change.style.font = 'bold';
}
</script>
</body>
</html>
```

