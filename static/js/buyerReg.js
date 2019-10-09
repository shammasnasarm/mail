<%@ page contentType="text/html; charset=iso-8859-1" language="java" import="java.sql.*" errorPage="" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>Untitled Document</title>

</head>

<body>
	<script type="text/javascript">
		function validation()
		{
			var alpha=/^[a-zA-Z]+$/;
			var num=/^[0-9]+$/;
			
			var email=/^[\w\-\.\+]+\@[a-z A-Z 0-9\.\-]+\.[a-z A-Z 0-9]{2,4}$/;
			
			var nam=document.getElementById("txtname");
			var dob=document.getElementById("txtage");
			var mail=document.getElementById("txtMail");
			var mob=document.getElementById("txtMob");
			var unme=document.getElementById("txtUname");
			var psw=document.getElementById("txtPass");
			var conps=document.getElementById("txtCpass");
			var m=document.myform.radgen;
		//varbl=	m[0].checked;
		if(m[0].checked==false && m[1].checked==false)
		{
			alert("Please Enter your gender ");
			return false;
		}
//			if(m[0].checked==false && m[1].checked==false)
//			{
//			alert("Please Enter your gender ");
//				return false;
//			}
			
			if(nam.value.length==0)
			{
				alert("Please Enter your name ");
				return false;
			}
			else if(!nam.value.match(alpha))
			{
				alert("invalid name");
				nam.focus();
				return false;
			}
			
			else if(plc.value.length==0)
			{
				alert("Place field cannot be null");
				return false;
			}
			else if(!plc.value.match(alpha))
			{
				alert("invalid character in place field");
				plc.focus();
				return false;
			}
			else if(mail.value.length==0)
			{
				alert("Email field cannot be null");
				return false;
			}
			else if(!mail.value.match(email))
			{
				alert("invalid mail id");
				mail.focus();
				return false;
			}
			
			else if(mob.value.length==0)
			{
				alert("Mobile field cannot be null");
				mob.focus();
				return false;
			}
			
			else if(!mob.value.match(num))
			{
				alert("invalid mobile number");
				mob.focus();
				return false;
			}
			else if(unme.value.length==0)
			{
				alert("Username field cannot be null");
				return false;
			}
			else if(psw.value.length==0)
			{
				alert("Password field cannot be null");
				return false;
			}
			else if(!conps.value.match(psw.value))
			{
				alert("PASSWORD DO NOT MATCH");
				conps.focus();
				return false;
			}
			
			else
			{
				return true;
			}
		}	
			
		
	</script>
	
	
	
	<form method="post" action="buyerAction.jsp" name="myform">
		<table align="center" cellspacing="7">
		<caption><strong>BUYER REGISTRATION</strong></caption>
		<tr>
			<td width="64">Name:</td>
			<td width="182"><input type="text" name="txtname" id="txtName"/></td>
		</tr>
		<tr>
			<td>Place:</td><td><input type="text" name="txtplace" id="txtPlace" /></td>
		</tr>
		<tr>
			<td>Email:</td><td><input type="text" name="txtmail" id="txtMail" /></td>
		</tr>
		<tr>
			<td>Mobile:</td><td><input type="text" name="txtmob" id="txtMob"  /></td>
		</tr>
		<tr><td>Gender:</td><td><input type="radio" name="radgen" id="radGen" value="male"/>Male
								<input type="radio" name="radgen" id="radGen" value="female"/>Female
							</td></tr>
		
		<tr><td>Username:</td><td><input type="text" name="txtuname" id="txtUname"/></td></tr>
		<tr><td>Password:</td><td><input type="password" name="txtpass" id="txtPass"/></td></tr>
		<tr><td>Cofirm Password:</td><td><input type="password" name="txtcpass" id="txtCpass" /></td></tr>
		<tr>
			<td colspan="2" align="center"><input type="submit" name="subBuyer" value="Register" id="subBuy" onclick="return validation()"/></td>
		</tr>
					
		</table>
		
	</form>
	<%
		String mssg=request.getParameter("msg");
		if(mssg!=null && mssg=="Success")
		{
			out.print(" Buyer Successfully Registered");
		}
	%>
	
</body>
</html>
