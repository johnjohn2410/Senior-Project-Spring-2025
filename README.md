# Senior-Project-Spring-2025
This is to showcase our final project for our Computer Science degree.

## **Course Evaluation Dashboard Project** ##

## Overview
The Course Evaluation Dashboard is a web application designed to provide UTRGV students with a centralized and interactive platform to review course evaluation data. This project aims to enhance transparency and informed decision-making in course selection by presenting aggregated evaluation metrics for students whiole they are registering for classes.

---

## Features
1. **Data Scraping**
   - A Python-based web scraper fetches course evaluation data from UTRGV’s API.
   - Extracted data is parsed and stored for analysis and visualization.

2. **Data Cleaning**
   - Inconsistencies and missing values in the scraped data are handled.
   - Data is processed to generate aggregated insights for easier interpretation.

3. **Web Application**
   - Responsive and user-friendly interface for students.
   - Advanced search and filtering options for professors, courses, and semesters.
   - Visualization of evaluation trends and downloadable reports.

---

## Tech Stack
- **Frontend**: React.js(maybe/TBD)
- **Backend**: Node.js / Django (TBD)
- **Data Analysis**: Python (Pandas, Matplotlib)
- **Web Scraping**: Python (requests, json, AJAX)
- **Deployment**: Vercel / AWS (TBD)

---

## How It Works
1. **Web Scraper**:
   - Fetches raw data from UTRGV’s course evaluation API using AJAX requests.
   - Handles JSON responses to extract relevant fields like instructor ratings and comments.
2. **Data Cleaning**:
   - Processes the raw data to remove null values and outliers.
   - Aggregates metrics such as average scores and enrollment data.

3. **Dashboard**:
   - Displays evaluation data with an intuitive and responsive UI.
   - Offers visualizations like bar charts and trend lines for analysis.

---

## Challenges
- **Data Quality**: Handling missing or inconsistent data in evaluation reports.
- **API Handling**: Managing large datasets and handling potential API failures or rate limits.
- **User Experience**: Creating an intuitive and visually appealing dashboard.

---

## Future Enhancements
1. Implement authentication for restricted access.(TBD)
2. Add support for exporting data (e.g., CSV or PDF). (TBD)
3. Provide user feedback mechanisms for additional feature requests. (TBD)

---

## Installation Instructions
1. Clone this repository:
   ```bash
   git clone [https://github.com/johnjohn2410/Senior-Project-Spring-2025]
   ```

2. Install dependencies:
   ```bash
   cd [Senior-Project-Spring-2025]
   npm install  # For frontend
   pip install -r requirements.txt  # For backend and data scripts
   ```

3. Run the scraper to populate the database:
   ```bash
   python WebScraper.py
   ```

4. Start the application:
   ```bash
   
   ```

---

## Contributors
- [John Ross] - 
- [Daniel Gutierrez]
- [Joe Reyna]
- [Esteban Kott]

---

## Contact
For questions or suggestions, please contact daniel.gutierreziii01@utrgv.edu, john.ross01@utrgv.edu, Esteban.kott01@utrgv.edu, joe.reyna02@utrgv.edu

