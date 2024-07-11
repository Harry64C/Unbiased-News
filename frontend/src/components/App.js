import React, { Component } from "react";
import { createRoot } from 'react-dom/client';
import {useState, useEffect} from 'react'
import 'bootstrap/dist/css/bootstrap.min.css'

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return <h1>Testing React</h1>
    }
}

const domNode = document.getElementById('app');
const root = createRoot(domNode);
root.render(<App />);