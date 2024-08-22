---
sidebar_position: 1
---
# Using the Mission Activator: How To Create Missions And Add Them Into The Board

After working on the mission activator as I go from the previous leader, I am noting down tips and tricks as I go to ensure smooth sailing in creating scripts for missions without any problems. Any difficulties that have been solved throughout the process will be recorded so juniors will not make the same mistakes. Anyone else is free to note any problems in relation with their own scripts being used in the mission activator.

This is with the assumption that you already created your own mission scripts in the Unity Project and need to add them to the mission activator. To start off, here is the video that will help you understand at first:

[Unity Mission Activator](https://deakin365.sharepoint.com/sites/RedbackOperations9/_layouts/15/stream.aspx?id=%2Fsites%2FRedbackOperations9%2FShared%20Documents%2FHowToAddAMission%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E4a8e6eb1%2D2f43%2D44ee%2Dbbeb%2D492704e87eff)

Before you start working on any missions, note that you should be able to put your script in an empty object and it should still function correctly otherwise you are going to have to upgrade it that way later which is more work for you.

If you have already added the missions into the activators and found out that your script is not working compared to say, adding the script directly to the bike as a means to testing it out, there are a few reasons for that:

- For the bike, there is a need to collect items, press buttons or bump into things that usually when the script is directly added into the bike for mission testing purposes, any collision function is used such as OnTriggerEnter for the interaction. However, that will only work when the script is added directly to the bike. With the Mission Activator using an empty object to store the mission script, alternate ways can be used depending on the mission's content in the update function. 
- To collect items, finding game objects with tags such as FindGameObjectsWithTag() and FindWithTag() functions for array and a singular item respectively as well as using activeSelf for the gameObject that is set to false to indicate the item's removal thanks to the bike is a good start for an alternate way from the collision function but still a guideline depending how the mission is created.
- SetActives are also important parts in mission because they can detect the success of the mission by the object's in the area. To understand the meaning better, please refer to previous missions such as Mission 1 and Mission 5 in Unity.

When testing the missions, there are a few things with the mission activator that you should consider:
- Make sure that all empty objects with missions are placed inside Objectives > Missions for the missions to work. Any game object (not prefab) should be added alongside your mission empty objects so they can be used such as Mission 1 with robot and b (non prefab game objects). If robot and b were put anywhere else, they will black out and not work.
- Make sure that there are missions on the list. If the mission list is empty, they will run all the missions in the file as the mission list serves as an activator / deactivator
