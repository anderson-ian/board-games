# boardGames

## Overview

This is my new Kedro project, which was generated using `Kedro 0.17.6`.

The main aim of this project is to engineer from a multi-table input dataset a data pipeline. I have been working hard through DataCamp's Data Engineering Career track. It is phenomenal, and the amount of information and applied problems really gels well for the most part. It just flows pretty well. At the same time, it truly is a dearth of information and I can feel it slipping away without application. So this project aims to simply put bits to bytes and try to solidify the progress I have made over there.

 I enjoy board games, and I like the open data concept of TidyTuesday, so I decided to dive into my first Data Engineering problem to combine these worlds. The dataset contains ratings by game, and then details about each game. 

The source of the data is https://github.com/rfordatascience/tidytuesday/tree/master/data/2022/2022-01-25 

There's a nice exploration walkthrough here:

https://jvanelteren.github.io/blog/2022/01/19/boardgames.html

## What I Did

The dataset is pretty rich and involves a ton of potential features, including raw text describing the rules of the games. There's really a lot there. Primarily though, I was trying to get a very basic implementation of `kedro` up and running. I wanted to use this data science framework because it solves many of the problems of collaborative data science. 

I wanted to try it out in the most basic of implementations. My requirements were to 1) Don't Repeat Yourself (DRY), 2) separation of concerns, 3) use PowerShell to access the data and 4) writing unit tests. A final potential concept was Data Version Control (DVC) but this really didn't take off for me. I had bit off enough just by trying to get myself through writing tests and orchestrating the pipeline. In future, I would gladly try to expand the pipelines, try out DVC, and also take a look at `great_expectations` for data control.

- What went well?

I think I did pretty well to do only one thing with each function in my data preprocessing nodes. I found the process of prototyping functions and behaviors in the `kedro notebook` Jupyter Notebook instance really intuitive. From there, it was pretty easy to bring the code back into the `nodes.py` file and define functions. Then adding these to the runner framework was also pretty easy. 

I was pretty happy with the simple tests that I wrote. I used simple dataframes to ensure that expected behaviors with the data manipulations were happening correctly. This is huge for me, as I have not been as thorough as this in the past. I can really see how this important step would pay huge dividends in a collaborative setting (A: with peers, and B: with my future self).

I was also glad to use PowerShell to download the data from GitHub. While this is an odd use case, it meant that I could check the download code into version control, and another Windows user could make it useful in future on their own machine (assuming the data has not moved). It's scripted magic, without having to set up a complex Kedro implementation to access a custom dataset. I just am simply not at that level yet.

- What could go better?

I think I did well to use pseudo-data in the tests I wrote. I have never run tests before, and for these I wrote them after the fact. In future I would actually probably write the tests first, before even writing `def my_function_name(): pass`. Getting the tests down using pseudo data is a fundamentally different way to thinking about code. I am excited to see where this takes me. 

Obviously, it would be really important to set up models and take this to the next level. But right now, my main focus is on simple data processing that can replace Excel AND can scale to all that cool stuff that's possible when data engineering becomes predictable, reproducible, and collaborative. Kedro, git,pytest, great_expectations, and possibly DVC all seem to enable that. There's no reason to regress into Jupyter Notebook chaos. That's just an Excel transplant. It's all fun and games until you have to productionize your code and/or share it with your peers. And testing. If it can go wrong, it will go wrong.

Finally, I think that this framework approach allows for incremental improvements. With this code, testing, and data validation (eventually), making enhancements and breaking ground on something new isn't so scary anymore. It just is part of the framework. That way, an enhancement doesn't involve bringing the entire pipeline into the work cue to be tested top to bottom. If code matches, and tests don't fail, a small improvement can be implemented without massive hassle. Code can be repurposed to new projects and ideas. 