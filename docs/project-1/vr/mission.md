---
sidebar_position: 3
---
# Using the Mission Activator

## How To Create Missions And Add Them Into The Board

After working on the mission activator as I go from the previous leader, I am noting down tips and tricks as I go to ensure smooth sailing in creating scripts for missions without any problems. Any difficulties that have been solved throughout the process will be recorded so juniors will not make the same mistakes. Anyone else is free to note any problems in relation with their own scripts being used in the mission activator.

This is with the assumption that you already created your own mission scripts in the Unity Project and need to add them to the mission activator. To start off, here is the video that will help you understand at first:

[Unity Mission Activator](https://deakin365.sharepoint.com/sites/RedbackOperations9/_layouts/15/stream.aspx?id=%2Fsites%2FRedbackOperations9%2FShared%20Documents%2FHowToAddAMission%2Emp4&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E4a8e6eb1%2D2f43%2D44ee%2Dbbeb%2D492704e87eff)

Before you start working on any missions, note that you should be able to attach your script in an empty object and it should still function correctly otherwise you are going to have to upgrade it that way later which is more work for you.

If you have already added the missions into the activators and found out that your script is not working compared to say, adding the script directly to the bike as a means to testing it out, there are a few reasons for that:

- For the bike, there is a need to collect items, press buttons or bump into things that usually when the script is directly added into the bike for mission testing purposes, any collision function is used such as OnTriggerEnter for the interaction. However, that will only work when the script is added directly to the bike. With the Mission Activator using an empty object to store the mission script, alternate ways can be used depending on the mission's content in the update function. 
- To collect items, finding game objects with tags such as FindGameObjectsWithTag() and FindWithTag() functions for array and a singular item respectively as well as using activeSelf for the gameObject that is set to false to indicate the item's removal thanks to the bike is a good start for an alternate way from the collision function but still a guideline depending how the mission is created.
    - An example code for item collection using finding game object with tags:
      ```C#
      //Finding an array of stars. Game tag made at the star prefab as 5.
      GameObject[] starFind = GameObject.FindGameObjectsWithTag("5");
      //Once the array reaches 0, all stars are collected.
      if(starFind.Length == 0)
      {
          Debug.Log("All stars are found");  
      ```
- SetActives are also important parts in mission because they can detect the success of the mission by the object's in the area. To understand the meaning better, please refer to previous missions such as Mission 1 and Mission 5 in Unity.
    

When testing the missions, there are a few things with the mission activator that you should consider:
- Make sure that all empty objects with missions are placed inside Objectives > Missions for the missions to work. Any game object (not prefab) should be added alongside your mission empty objects so they can be used such as Mission 1 with robot and b (non prefab game objects). If robot and b were put anywhere else, they will black out and not work.
- Make sure that there are missions on the list. If the mission list is empty, they will run all the missions in the file as the mission list serves as an activator / deactivator
- When making missions in different scenes, make sure the Objectives from City Scene is copied to the new scene, if haven't already, and from the Mission Activator script, make sure that the list has the same number of elements in each scene. it is OK for the element to be blank for the particular mission that is on a specific scene. 
- For point above, only work on any missions in CityScene until other scenees are stated useable for testing purposes (Pending for other scenes)

## Future Development

A modification has been made to the Mission_Activator script in that it will now find all Missions in a scene and automatically add them to the activation system.

To create your Mission, instead of extending from MonoBehaviour like you would normally, the following base class has been created that handles a way to find missions and have the name and number stored:
```C#
public class Mission : MonoBehaviour
{
    public virtual int MissionNumber => 0;
    public virtual string MissionName => "Not Set";
}
```
To create a child class that will be found by the activator, use code similar to below which is implemented in the Mission1 script:
```C#
public class Mission1 : Mission
{
    public override string MissionName => "Collect the Star";
    public override int MissionNumber => 1;
```
