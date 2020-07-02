import React, {Component} from 'react';
import axios from "axios";

// import Navbar from "./navbar1.component"

export default class ChangePassword extends Component {
    constructor(props) {
        super(props)

        this.state = {
            password: "",
            confirmpassword: ""
        }
        this.onChangePassword = this.onChangePassword.bind(this);
        this.onChangeConfirmPassword = this.onChangeConfirmPassword.bind(this);
        this.onSubmit = this.onSubmit.bind(this);
    }

    onChangePassword(e) {
        this.setState({password: e.target.value});
    }

    onChangeConfirmPassword(e) {
        this.setState({confirmpassword: e.target.value});
    }

    validatePassword(inp) {
        if (inp.length >= 6 && inp.match(/[A-Z]/) && inp.match(/[a-z]/) && inp.match(/[0-9]/) && inp.match(/[!@#$%^&*()_+\-=\\[\]{};':"\\|,.<>\\//?]+/)) {
            return true
        } else {
            alert("please enter a valid password in which it should consist of one upper case letter, one lower case letter," + 
            "one number, one special character and min length should be 6 chars");    //The pop up alert for a valid email address
            return false;
        }
    }

    onSubmit(e) {
        e.preventDefault();

        if(this.state.password !== this.state.confirmpassword){
            alert("The passwords doesn't match")
            return false; // The form won't submit
        }

        if (this.validatePassword(this.state.password)) {
            const User = {
                password: this.state.password
            }
            console.log(User)
            axios.post('http://localhost:5000/changepassword', User)
            .then(res => {
                if (res.data.message === 'password updated!') {
                alert(res.data.message)
                window.location = '/profile'
            }
        });
    }
}
    render() {
        return (
            <div>
                {/* <Navbar /> */}
            <form onSubmit = {this.onSubmit}>
                <h3>ChangePassWord</h3>
                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" name = "password" autoComplete="password" onChange = {this.onChangePassword} required />
                </div>
    
                <div className="form-group">
                    <label>Confirm password</label>
                    <input type="password" className="form-control" placeholder="Re enter password" name = "password" autoComplete="password" onChange = {this.onChangeConfirmPassword} required/>
                </div>
    
                <button type="submit" className="btn btn-primary btn-block">Submit</button>
            </form>
            </div>
        );
    }
}