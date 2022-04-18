
## data source: structure and unstructured

structured data: SQL databases, online transactional processing(OLTP),
spreadsheets, online forms, sensor GPS and RFID, network and web
server logs

semi-structured data: email, XML, other markup languages, binary executabsles, TCP/IP packets, zipped files, JSON. XML, JSON are used to store semi-structured data that defines tags, attributes or to store data(mega tags for grouping and hierarchy)

unstructured data: have no identifiable structure: cannot be stored in relational databases: web pages, social media feeds, images in varied file formats, video and audio files, documents and pdf files, powerpoint presentations, media logs and surveys. (files, no sql databases)

## file formats
1. delimited text file formats, or .CSV
*data stored as text
*value is separated by a delimiter
*CSV(comma-serparated values) TSV(tab-separated values)


2. Microsoft Excel Open .XML Spreadsheet, or .XLSX
AKA excel worksheet

3. Extensible Markup Language, .XML
*markup language for encoding data
*similar to .HTML
*platform, programming language independent
*data is shared easily across systems

4. portble document language, .PDF

5. Javascript Object Notation, Json
1 language-independent 
2 compaitble across wide range of browsers

## data sources
1. relational databases: structure data
2. flat files: plain text, separated by delimiter, single table
3. spreadfiles: tabular format, .XLS. .XLSX. 
4. XML files: using tags
5. APIS and Web services: 
6. web scraping 
7. data streams and feeds : social media feeds

*relational databases*
1. taublar forms(rows and columns)
2. well defines structure and schema 
3. optimized for data operation and querying 
4. SQL as the standard language 
5. relating tables based on common data
6. understand relationship between different data
7. for large volume of data
8. mimilize dara redundance
9. security architecture provides greater access control
10. example

![[DBMS examples.png]]

11. advantage: join tables, flexibility, minimize data redundancy, easy backup, 
12. used for online transaction processing application(OLAP); data warehouses(OLAP); IOT
13. limition: not suitable for semi-structured; migration is quite limited; limitation of the storage 

*non- relational databases(Nosql)*
1. diverse data form
2. built for speed, flexiblity 
3. big data, cloud computing, mobile applications 
4. not only 
5. flexible schemas
6. four types: key-value, document based, column based, graph based: 


*data warehouses*
1.  data from different sources 
2. store analysis-ready data 
3. 3 tier architecture: 1. detabase servers(extra data from different sources) 2. process and analyze information from database servers. 3. client fron-end layer(querying, reporting and analyzing data)
4. are moving to the cloud: lower costs, limitless compute capabilities, faster disaster recovery.
5. data mart: part of data warehouses: dependent; independent; hybrid. purpose: provide data direcly to users.

*Data Lake*
chaos; as a repository of raw data



*big data stores*
1. distributd system

# summary

In this lesson, you have learned:

A Data Repository is a general term that refers to data that has been collected, organized, and isolated so that it can be used for reporting, analytics, and also for archival purposes.

The different types of Data Repositories include:

-   Databases, which can be relational or non-relational, each following a set of organizational principles, the types of data they can store, and the tools that can be used to query, organize, and retrieve data.
    
-   Data Warehouses, that consolidate incoming data into one comprehensive store house.
    
-   Data Marts, that are essentially sub-sections of a data warehouse, built to isolate data for a particular business function or use case.
    
-   Data Lakes, that serve as storage repositories for large amounts of structured, semi-structured, and unstructured data in their native format.
    
-   Big Data Stores, that provide distributed computational and storage infrastructure to store, scale, and process very large data sets.
    

The ETL, or Extract Transform and Load, Process is an automated process that converts raw data into analysis-ready data by:

-   Extracting data from source locations.
    
-   Transforming raw data by cleaning, enriching, standardizing, and validating it.
    
-   Loading the processed data into a destination system or data repository.
    

The ELT, or Extract Load and Transfer, Process is a variation of the ETL Process. In this process, extracted data is loaded into the target system before the transformations are applied. This process is ideal for Data Lakes and working with Big Data.

Data Pipeline, sometimes used interchangeably with ETL and ELT, encompasses the entire journey of moving data from its source to a destination data lake or application, using the ETL or ELT process.

Data Integration Platforms combine disparate sources of data, physically or logically, to provide a unified view of the data for analytics purposes

apache hadoop: a collection of tools that provide distributed storage and processing of big data: 

apache hive: a data warehouse for data query and analysis built on top of hadoop

Apache Spark: a distributed analytics framework for complex real-time data analytics



