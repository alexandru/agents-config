# Support harness-native reminder event conditions

Reminder rules may include harness-native lifecycle events as conditions alongside tool counts and elapsed time. An event condition remains satisfied within its rule's interval until that interval resets, and delivery waits for a non-blocking, model-visible hook. This recalls prompt obligations around lifecycle transitions without requiring token measurements or treating the event as proof that the associated operation succeeded.
