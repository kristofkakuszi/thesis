import React from 'react'
import loginImg from "../../login.svg"

export class Register extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        return(
        <div className="base-constainer">
            <div className="header">Register</div>
            <div className="content">
                <div className="image">
                    <img src={loginImg} alt="" />
                </div>
                <div className="from">
                    <div className="form-group">
                        <label htmlFor="username">Username</label>
                        <input type="text" name="username" placeholder="username" />
                    </div>
                    <div className="form-group">
                        <label htmlFor="email">E-mail</label>
                        <input type="email" name="email" placeholder="email" />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Password</label>
                        <input type="password" name="password" placeholder="password" />
                    </div>
                </div>
            </div>
            <div className="footer"> 
                <button type="button" className="btn">
                    Register
                </button>
            </div>
        </div>
        )
    }

}