<?php
/**
	* This is a sample script which takes data from
	* your Google+ account and displays it !
	* @author Dhruv Baldawa (http://www.dhruvb.com/)
	* @license Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.(http://creativecommons.org/licenses/by-nc-sa/3.0/)
	* @copyright Dhruv Baldawa (http://www.dhruvb.com/)
*/	
  // Begin the session
  session_start();
// Declaring the variables required for authentication
	$client_key = '';
	$client_secret = '';
	$api_key = '';
	$redirect_uri = '';

// Check if the authorization code is received or not !
// Also, if the access token is received or not
	if (!isset($_REQUEST['code']) && !isset($_SESSION['access_token'])) {
		// Print the below message, if the code is not received !
		echo "Please Authorize your account: <br />";
		echo '<a href = "https://accounts.google.com/o/oauth2/auth?client_id='. $client_key. '&redirect_uri='.$redirect_uri .'&scope=https://www.googleapis.com/auth/plus.me&response_type=code">Click Here to Authorize</a>';
	}
	else {
    if(!isset($_SESSION['access_token'])) {
		  // Initialize a cURL session
		  $ch = curl_init();
		
		  // Set the cURL URL
		  curl_setopt($ch, CURLOPT_URL, "https://accounts.google.com/o/oauth2/token");

		  // The HTTP METHOD is set to POST
		  curl_setopt($ch, CURLOPT_POST, TRUE);

		  // This option is set to TRUE so that the response
		  // doesnot get printed and is stored directly in 
		  // the variable
		  curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
		
		  // The POST variables which need to be sent along with the HTTP request
		  curl_setopt($ch, CURLOPT_POSTFIELDS, "code=" . $_REQUEST['code'] . "&client_id=" . $client_key . "&client_secret=" . $client_secret . "&redirect_uri=".$redirect_uri."&grant_type=authorization_code");
		
		  // Execute the cURL request		
		  $data = curl_exec($ch);

		  // Close the cURL connection
		  curl_close($ch);

		  // Decode the JSON request and remove the access token from it
		  $data = json_decode($data);

		  $access_token = $data->access_token;
		  
		  // Set the session access token
		  $_SESSION['access_token'] = $data->access_token;
    }
    else {
      // If session access token is set
      $access_token = $_SESSION['access_token'];
    }
		// Initialize another cURL session
		$ch = curl_init();

		// Set all the options and execute the session
		curl_setopt($ch, CURLOPT_URL, "https://www.googleapis.com/plus/v1/people/me?access_token=" . $access_token);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
		$data = curl_exec($ch);
		curl_close($ch);
		// Get the data from the JSON response
		$data = json_decode($data);
		
		// Show the output
		echo "<img src = \"". $data->image->url . "\" /> <br />";
		echo "<pre>";
		echo "========================================= <br/>";
		echo "  + Hello " . $data->displayName . "<br />";
		echo "  + I am shocked you are " . $data->relationshipStatus . " ! <br />";
		echo "  + I know something about you: <br />";
		echo $data->aboutMe . "<br />";
		echo "========================================= <br />";
		echo "Author: @dhruvbaldawa <br />";
		echo "</pre>"; 
		echo "You are successfully authorized.";
	}	
?>
