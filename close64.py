#!/usr/bin/env python3
import sys
import PySimpleGUI as sg

# Usage of icons as base64 string and toolbar

close64 = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsSAAALEgHS3X78AAAE30lEQVRIiZ2VXYgdRRqGn6+quvucM/85iRoTNevMBJFEWY0GFQTBC1HBlaz/jMpoFFfXBdmFvdiLvRIEFRHFGBXMjUQhF/6Bol6sSNaIruCNir/R/Dlx5iRzck736e6qby/6JDlx9CIWFN10Ue/7vW+9X7XcDn8bryWPL2vERkNQQPj9Q72K7F3s7Hxb9bZ98L0bj91jt1y23kxNTxIEGUQ/aTYR6WW9cud/Prx01zf7/7FP5EHXHG7Y6bVTpBPLMSegCWKEEMKvkihgjEWDP+FbEjxTa1bjv9l/CsIKF3ypHhUDSFGACCKC956iKKjV6/hfkCjgUNK0TW1oCA3h+EJk8UUBYFCsQaSyRajArUWLnEONcTrT68nTLtZaEKmmMTiUlsREGy9HO0dgcL1y6lgtZrAsEYFexhwxq2buYfru+1mcOo+828UYg4rgUH7OSkY3zbDq1lkaV1yFP9TqEyy18jiBCMF7DjYmOOu+hxifnCSKItZuvp/F6fPJ05TEwE+dHhN33MfpGy4iFAVjf7qF8etvBV9y1IilBApGIMt6TExOM372JKqKqhLFMdOz93Jk6jx+bHVoztzLyj9eiHqP2Gq7O3UlGAuq1RwYDlUwhoChMdSAz3ZxaEeD8T/fBggaAnGtxpqZWdKFBSbOPLMCCQGJItJPdrHw4lOYRgNsBM6dSCDGErIuodtGkhoyPEr68U5svcbI1ZsQY0CV2vAw9ZGRKjEiSBTR/fQjDm9/AddcjqoSul182kYHVDhJauRffUH7wD7ilatxzVOwI6PM7XiJLO2x4rob0CgGVTSEKigidD94j/ltW9Dg0b0/4BfmyQ8ewKUdWLZ6wCIB9SXFXJvQ+hLkc6QeEznHf199jY1rpjh1w0ZUFTGm7z18/tSj2Hffor5shKLdhhJCADMcw7IlKRIkAqkJRIa4LPl6d5c/PPJkBd5vpArcArD+ue101l1Md08bFxuIBUlOyOUggUIAVIl94Kv5wKqtz7L+7r/0bRHEmApcFbwnHhljw6tv0b3kEtK5gDWmj/GbfQAWZbdaztjyPOfP3oN6D8GDCO133uDAvx9CyxKsRX1JMjbBBa+8Rnbl5RSpR35RfXUGfVLnYGFBcTfdwLo77yLkPYy14CLa773JngfuoNy7QOh2WPnw09WVkufUm8s598G/s+eT9wmBJZ1m+sVTFNBc4Wi8vJ3v//kAJk7AOhbf3MGezTfjWwuYCcv8s1s58K+/okWOxDGdjz5g7+YZtKRSoL+igCp5FKVntGk48sTTzDWb1C+4mB833wgETD2CELBjEfNbtyAjo4xdcz27N11L6B5GGoZQhN+26KiSoII9LebnJx9BkggzNIQkyfEdItiRQGvbM7S2bQHJMGN1NO8ds2dQhBORYBCjAFEE1kFSw0QxuAiTJCAGce64vz4gviTkOTJcErIMMRbyDIxg7bHTFnc47clcmpdj43VkeBRJEkytgdTqSL2OiRMkSRDroH9t4EtCUaBZhmYpIUurZ9pFfVnuX+w62xfjeq3D3/6vbifXrT1XkzgWdREmipA4RlwMUYRY21cg/X+lJ5gSbIHGOVovCHmOCSX7DrbMx599icIhVI2cA5c5mC1gbGnITm4oqAOr0PoOXs9g51HAGiITyCDByXDp4KuiaoESmP8/YC0Y5GajmEsAAAAASUVORK5CYII='