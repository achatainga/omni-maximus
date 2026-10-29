import React, { useState } from "react";

/**
 * Trap 4: Click-Path State Cancellation (FE-3)
 * Function A sets state, Function B silently cancels it in the same handler.
 */
export function UserProfileModal({ user, onClose }: any) {
  const [isSaved, setIsSaved] = useState(false);
  const [activeTab, setActiveTab] = useState("profile");

  const resetModalState = () => {
    setActiveTab("profile");
    setIsSaved(false); // SILENT CANCELLATION SIDE EFFECT
  };

  const handleSaveAndExit = async () => {
    // Step 1: User saves profile
    setIsSaved(true);
    
    // Step 2: Modal cleanup is called
    resetModalState(); // Silently reverts isSaved back to false!
    
    onClose();
  };

  return (
    <div>
      <button onClick={handleSaveAndExit}>Save and Exit</button>
      {isSaved && <span className="toast">Profile Saved Successfully!</span>}
    </div>
  );
}
