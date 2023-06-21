## nmapXml2txt

The `nmapXml2txt` script is a tool written in Python 3 that allows you to convert Nmap's XML output file into a more readable and easily analyzable plain text format. It facilitates the extraction of relevant information from the scan results, such as IP addresses and open ports.

### Installation

1. Make sure you have Python 3 installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

2. Download the `nmapXml2txt.py` file from the repository.

3. There are no external dependencies required for this script as it uses Python's standard libraries.

### Usage

The `nmapXml2txt` script is executed from the command line and accepts an Nmap XML output file as an argument. The general syntax is as follows:

```
python3 nmapXml2txt.py <xml_file>
```

Where `<xml_file>` is the path or name of the actual Nmap XML output file you want to process.

### Example Usage

1. Open a terminal and navigate to the location where the `nmapXml2txt.py` script is located.

2. Run the following command to process an Nmap XML output file:

```
python3 nmapXml2txt.py results.xml
```

Make sure to replace `results.xml` with the actual path or name of your XML file.

3. The script will process the XML file and generate a plain text file with the extracted information. The output file will be saved in the same directory as the XML file, with the name `results.txt`.

4. Open the `results.txt` file in a text editor to view the results in a readable format.

### Generated Output

The `nmapXml2txt` script will generate a plain text file with the following structure:

```
IP Address: Port
IP Address: Port
...
```

Each line represents an IP address and its associated port. This output makes it easy to identify the IP addresses and open ports found during the Nmap scan.

### Limitations

- The script is specifically designed to process Nmap XML output files in the standard format. Other formats may not be supported.
- Only IP addresses and open ports are extracted from the XML file. Other scan details such as hostnames or service information are not included in the output.

### Contributions

If you would like to contribute to the development of `nmapXml2txt` or have any improvement suggestions, feel free to submit a pull request or open an issue on the official repository: [link to repository](https://github.com/your_username/nmapXml2txt)

### License

This project is distributed under the MIT License. See the `LICENSE` file for more information.

### Contact

If you have any questions or inquiries related to `nmapXml2txt`, you can reach me via email at your_email@example.com

I hope you find this tool helpful. Thank you for using `nmapXml2txt`!
