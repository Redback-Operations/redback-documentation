**Ball annotations with CVAT**

Ball annotations are slightly different to player annotations. For ball
annotations, we are training a model which can predict the trajectory of
the ball, but also where the ball location is even under full occlusion.

\"**occlusion**\" refers to the visibility status of an object within an
image or video frame, indicating whether the object is partially or
fully obstructed.

**Partially occluded**

If the ball is partially occluded, you mark it as occluded using the
"occluded property". Partially occluded means the ball is visible, but
is obstructed by something

**Fully occluded**

If the ball is fully occluded, mark it as occluded using the occluded
property, as well as marking it as fully occluded using the checkbox in
the details section.

**Out of frame**

If a ball it out of frame, you can toggle the "out of frame" property
which removes the box annotations. When it becomes visible again, you
can then toggle it again.
