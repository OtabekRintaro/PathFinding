const DescriptionDisplay = (props) => {
    const description = props.description

    console.log('rendered');
    return (
        <div>
            <p>
                {description}
            </p>
        </div>
    );
};

export default DescriptionDisplay;