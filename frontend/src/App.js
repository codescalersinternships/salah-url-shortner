import { useState } from "react";
import './App.css';

function App() {
	// longURL holds the input provided by the user
	const [longURL, setLongURL]             = useState("");
	// shortURL holds the value of the short URL returned by the server
	const [shortURL, setShortURL]           = useState("");
	// copiedText used to toggle the text value of copying button
	const [copiedText, setCopiedText] 		= useState("");
	// status holds response status, it can be 'success' or 'error'
	const [status, setStatus] 	= useState("");
	// errorMessage holds response error message if response status is 'error'
	const [errorMessage, setErrorMessage] 	= useState("");

	const handleSubmit = (e) => {
		e.preventDefault();
		fetch("/api", {
			method:   "POST",
			body:     JSON.stringify({ longURL: longURL }),
			headers:  { "Content-Type": "application/json" },
		})
			.then((res)   => res.json())
			.then((data)  => {
				setShortURL(data.shortURL);
				setLongURL(data.longURL);
				setStatus(data.status);
				setErrorMessage(data.errorMessage);
			});
	};

	const handleCopy = (e) => {
		e.preventDefault();
		navigator.clipboard.writeText(shortURL).then(() => {
			setCopiedText(shortURL)
		})
  	}

	return (
		<div className="content-wrapper">

			<h1 className="page-title">URL Shortener</h1>

			<div className="page-description">
				Simple URL shortener application built with Django and React.
			</div>
			
			<div className="form-wrapper">

				<div className="input-wrapper">
					<input type="text" name="longURL" placeholder="https://..." onChange={(e) => setLongURL(e.target.value)}/>
				</div>
				
				<button type="submit" class="button" disabled={!longURL} onClick={(e) => handleSubmit(e)} >
					shorten
				</button>
			</div>

			{shortURL && status === "success" && (
				<>
					<h3 className="result-title">Shorten URL:</h3>

					<div className="result-link-wrapper">

						<a target="_blank" rel="noreferrer" className="shorten-url" href={shortURL} >
							{shortURL}
						</a>

						<button onClick={(e) => handleCopy(e)} className="copy-button">
							{copiedText === shortURL ? 'Copied!' : 'Copy'}
						</button>
						
					</div>
				</>
			)}
			
			{status === "error" && (
				<>
					{errorMessage && (
						<>
							<div class="alert">
								<strong>Error!</strong> {errorMessage}
							</div>
						</>
					)}
				</>
			)}

		</div>
	);
}

export default App;