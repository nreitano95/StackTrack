function confirmationMsg(e) {
    if(!confirm('Are you sure you would like to make these changes?')) {
      e.preventDefault();
      }
    }