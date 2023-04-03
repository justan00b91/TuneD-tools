if !([ -f "/etc/system-release-cpe" ]); then
	echo "No file named /etc/system-release-cpe"
	#read -p "Enter System type: " info
	#echo $(sed -n 's/CPE_NAME="//p' /etc/os-release | sed 's/.$//'):$info
	echo $(sed -n 's/CPE_NAME="//p' /etc/os-release | sed 's/.$//') > /etc/system-release-cpe
fi
echo "Done"
